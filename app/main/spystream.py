from main.lib.uasyncio.primitives.message import Message
from main.lib.uasyncio.primitives.queue import Queue
from uasyncio import create_task, sleep_ms, wait_for_ms, run, new_event_loop

from uasyncio.stream import Stream
from uasyncio.event import Event

import gc
gc.collect()

# This class:
#   Reads non blocking on rcv end of stream (a)
#   Writes on snd end of stream (b)
# snd|--->>|rcv
# 
class SpyStream(object):
    
    #TX clear to send event
    tx_cts = Event()
    _reading = Event()
    _writedata = Event()
    _writing = Event()
    _writewait = Event()
    
    rxq = Queue()
    txq = Queue()
    
    def __init__(self, read_func, write_func):
        print('SpyStream.__init__')
        self.stream_read = read_func
        self.stream_write = write_func
        self.read_task = create_task(self._read())
        self.write_task = create_task(self._write())
    
    async def _read(self):
        while True:
            try:
                self.tx_cts.clear()
                chunk = await wait_for_ms(self.stream_read(64), 10)
                self._reading.set()
                self.rxq.put_nowait(chunk)
            except:
                self._reading.clear()
                self.tx_cts.set()
            await sleep_ms(100)
        
    async def _write(self):
        while True:
            try:
                self._writedata.clear()
                data = await self.txq.get()
                self._writedata.set()
                self._writewait.set()
                await self.tx_cts.wait()
                self._writewait.clear()
                self._writing.set()
                self.stream_write(data)
                self._writing.clear()
            except:
                pass
    

class MasterSlaveSpy(object):
    
    def __init__(self, master_stream: Stream, slave_stream: Stream):
        self._master = SpyStream(master_stream.read, slave_stream.write)
        self._slave = SpyStream(master_stream.write, slave_stream.read)
        
    # Master events
    @property
    def evt_master_read_data(self):
        return self._master._reading
    
    @property
    def evt_master_cts(self):
        return self._master.tx_cts
    
    @property
    def evt_master_write_data(self):
        return self._master._writedata
    
    @property
    def evt_master_write_wait(self):
        return self._master._writewait
    
    @property
    def evt_master_write(self):
        return self._master._writing
    
    # Slave events
    @property
    def evt_slave_read_data(self):
        return self._slave._reading
    
    @property
    def evt_slave_cts(self):
        return self._slave.tx_cts
    
    @property
    def evt_slave_write_data(self):
        return self._slave._writedata
    
    @property
    def evt_slave_write_wait(self):
        return self._slave._writewait
    
    @property
    def evt_slave_write(self):
        return self._slave._writing

# Surround spystream with a IO gate that enables an AND gate to only get access to the line when needed so there's no pull-up on the lines
async def io_gate(pin_id, on_event, off_event):
    from machine import Pin
    pin = Pin(pin_id, Pin.OUT)
    pin.off()
    while True:
        await on_event.wait()
        pin.on()
        await off_event.wait()
        pin.off()
        await sleep_ms(0)

class GatedMasterSlaveSpy(MasterSlaveSpy):
    def __init__(self, master_stream: Stream, slave_stream: Stream, master_tx_pin, slave_tx_pin):
        super().__init__(master_stream, slave_stream)
        create_task(io_gate(master_tx_pin, self.evt_master_cts, self.evt_slave_read_data))
        create_task(io_gate(slave_tx_pin, self.evt_slave_cts, self.evt_master_read_data))
