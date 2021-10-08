# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(0) # redirect vendor O/S debugging messages to UART(0)

import webrepl
webrepl.start() # Enable webrepl
