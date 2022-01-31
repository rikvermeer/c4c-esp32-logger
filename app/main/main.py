import uasyncio
from machine import UART, Pin
from mqtt_as import mqtt_as
from esp32 import NVS
from parser import Parser, Message
#from network import WLAN, STA_IF
#from binascii import hexlify
from neopixel import NeoPixel

np = NeoPixel(Pi(14), 3)
np[0] = (0,128,0)
#np.write()

import gc
gc.collect()

#wlan = WLAN(STA_IF)
#client_id = str(hexlify(unique_id()))

nvs = NVS('lvlup')
def get_config(key):
    ba = bytearray(32)
    nr = nvs.get_blob(key, ba)
    return ba[:nr].decode()

def subs_cb(obj):
    print(obj)
    
config = mqtt_as.config
config.update({
    'server': get_config('mqtt_server'),
    'user': get_config('mqtt_user'),
    'password': get_config('mqtt_pass'),
    'ssid': get_config('wifi_ssid'),
    'wifi_pw': get_config('wifi_psk'),
    'subs_cb': subs_cb
})

connected = False
client = mqtt_as.MQTTClient(config)

async def onmessage():
    np[2] = (0,0,128)
    #np.write()
    await uasyncio.sleep_ms(10)
    np[2] = (0,0,0)
    #np.write()
    
async def onorder():
    np[3] = (128,0,128)
    #np.write()
    await uasyncio.sleep_ms(2000)
    np[3] = (0,0,0)
    #np.write()
    

async def run():
    try:
        await uasyncio.create_task(client.wifi_connect())
    except:
        pass
    try:
        await uasyncio.create_task(client.connect())
    except:
        pass
    
    def cb(res):
        #print('calback')
        for msg in res:
            #print('calback: ', msg.msg_type)
            if msg.msg_type == bytes([0x02, 0x01]):
            #if msg.msg_type == bytes([0x01, 0x01]):
                print('order', msg.body)
                uasyncio.create_task(onorder())
                #onorder()
                if client.isconnected():
                    uasyncio.create_task(client.publish('orders', 'cliq'))
                else:
                    print('Not connected')
    parser = Parser(cb)
    uam = UART(2, baudrate=38400, rx=27)
    master = uasyncio.StreamReader(uam)
    master.drain()
    while True:
        result = await master.read(32)
        parser.append_chunk(result)
        uasyncio.create_task(onmessage())
        #await uasyncio.sleep_ms(10)

async def led_writer():
    while True:
        np.write()
        await uasyncio.sleep_ms(5)

async def main():
    gc.collect()
    uasyncio.create_task(led_writer())
    uasyncio.create_task(run())
    
    while True:
        if client.isconnected():
            np[1] = (0,128,0)
            connected = True
        else:
            np[1] = (200,0,0)
            connected = False            
        await uasyncio.sleep_ms(500)
        
uasyncio.run(main())
