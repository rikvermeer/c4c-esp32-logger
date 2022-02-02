from machine import Pin
from neopixel import NeoPixel
np = NeoPixel(Pin(14),3)
np[0] = (128, 0,0)
np[1] = (0, 128, 0)
np[2] = (0, 0, 128)
np.write()

