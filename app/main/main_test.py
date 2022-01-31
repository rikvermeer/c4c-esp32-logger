import uasyncio
from machine import UART
from main.config import Config
from main.spystream import GatedMasterSlaveSpy
from main.parser import Parser, Message
from uasyncio.stream import Stream

cfg = Config()

class Runner(object):
    async def run_network(self):
        pass
    async def run_spystream(self):
        spy = GatedMasterSlaveSpy(
            Stream(UART(1, baudrate=38400, rx=26)),
            Stream(UART(2, baudrate=38400, rx=27)), 4, 5)
        while True:
            result = await spy.rxq.get()
            print(result)
    async def run_api(self):
        pass
    async def run_mqtt(self):
        pass
    async def run_forever(self):
        while True:
            #print('hello')
            await uasyncio.sleep_ms(500)

async def main():
   runner = Runner()  # Constructor creates tasks
   await runner.run_forever()  # Never terminates

def run():  # Entry point
    while True:
        try:
            uasyncio.run(main())
        finally:
            uasyncio.new_event_loop()
        
run()
