import uasyncio
from esp32 import NVS
from machine import RTC
from network import WLAN
from network import STA_IF
from ntptime import settime as settimeFromNTP

nvs = NVS('lvlup')
rtc = RTC()
sta_if = WLAN(STA_IF)


class TimeKeeper(object):
    def __init__(self, delay_seconds):
        self.loadRTCfromNVS()
        uasyncio.create_task(self.storeRTCtoNVSEvery(delay_seconds))
    
    def loadRTCfromNVS(self):
        print("Reading dt from NVS...")
        try:
            dt_year = nvs.get_i32('dt_year')
            dt_month = nvs.get_i32('dt_month')
            dt_day = nvs.get_i32('dt_day')
            dt_weekday = nvs.get_i32('dt_weekday')
            dt_hour = nvs.get_i32('dt_hour')
            dt_minute = nvs.get_i32('dt_minute')
            dt_second = nvs.get_i32('dt_second')
            dt_microsecond = nvs.get_i32('dt_microsecond')
            dt = (dt_year, dt_month, dt_day, dt_weekday, dt_hour, dt_minute, dt_second, dt_microsecond)
            rtc.datetime(dt)
            print("Read dt from NVS:", dt)
        except Exception as e:
            print("Time could not be retrieved", e)
            pass
    
    async def storeRTCtoNVSEvery(self, delay_seconds):
        while True:
            dt = rtc.datetime()
            try:
                nvs.set_i32('dt_year', dt[0])
                nvs.set_i32('dt_month', dt[1])
                nvs.set_i32('dt_day', dt[2])
                nvs.set_i32('dt_weekday', dt[3])
                nvs.set_i32('dt_hour', dt[4])
                nvs.set_i32('dt_minute', dt[5])
                nvs.set_i32('dt_second', dt[6])
                nvs.set_i32('dt_microsecond', dt[7])
                print("Stored dt to NVS: ", dt)
            except Exception as e:
                print("Time could not be stored", e)
                pass
            await uasyncio.sleep(delay_seconds)
            
class NTPTimerKeeper(TimeKeeper):
    
    def __init__(self, delay_write_seconds, delay_ntp_seconds):
        super().__init__(delay_write_seconds)
        uasyncio.create_task(self.readFromNTP(delay_ntp_seconds))
        
    async def readFromNTP(self, delay_seconds):
        while True:
            if sta_if.isconnected():
                print("WiFi connected, reading time from NTP")
                settimeFromNTP()
            else:
                print("WiFi NOT connected, NTP not available")
            await uasyncio.sleep(delay_seconds)
