import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import neopixel
import time

pixel_pin = board.D42
num_pixels = 1
pwr = DigitalInOut(board.NEOPIXEL_POWER)
pwr.direction = Direction.OUTPUT
pwr.value = True

pot = AnalogIn(board.A8) # set the pin to be an analog input

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

GREEN = (0, 255, 0)
OFF = (0, 0, 0)

while True:
    value = pot.value
    color_value = int((value / 65535) * 255)
    print(color_value)
    color = (color_value, 0, color_value)
    pixels.fill(color)
    pixels.show()
