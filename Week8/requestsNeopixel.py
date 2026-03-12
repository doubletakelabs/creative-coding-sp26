import time
import board
import wifi
import ssl
import socketpool
import adafruit_requests
import neopixel
from digitalio import DigitalInOut, Direction

import microcontroller

print()
print("Connecting to WiFi")

pixel_pin = board.D42
num_pixels = 1
pwr = DigitalInOut(board.NEOPIXEL_POWER)
pwr.direction = Direction.OUTPUT
pwr.value = True

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

GREEN = (0, 255, 0)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

#  connect to your SSID
wifi.radio.connect('WIRELESS_NETWORK_NAME_HERE', 'WIRELESS_PASSWORD_HERE')
print("Connected to WiFi")

url = "https://date.nager.at/api/v3/publicholidays/2026/US"
pool = socketpool.SocketPool(wifi.radio)

requests = adafruit_requests.Session(pool, ssl.create_default_context())

try:
    #  sends a request to the public holiday API
    response = requests.get(url)
    response_as_json = response.json()
    pixels.fill(GREEN)
    pixels.show()
    print(response_as_json)
    
except Exception as e:
    print("Error:\n", str(e))
    print("Resetting microcontroller in 10 seconds")
    pixels.fill(PURPLE)
    pixels.show()
    time.sleep(10)
    microcontroller.reset()
    
while True:
    pass