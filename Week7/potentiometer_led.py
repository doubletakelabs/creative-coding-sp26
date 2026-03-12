import board
from analogio import AnalogIn
import pwmio
import time 

analog_pin = AnalogIn(board.A8)
led = pwmio.PWMOut(board.D13)
MAX_BRIGHT = 61166 #change this to be your max value when you rotate your potentiometer

while True:
    value = analog_pin.value
    print(value)
    led.duty_cycle = value
    time.sleep(0.1) # debouncing! sleep 0.1 seconds
    