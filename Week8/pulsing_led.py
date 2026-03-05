import board
import pwmio
import time

# Set up the LED
led = pwmio.PWMOut(board.D13)

# Define our brightness limits
OFF = 0
MAX_BRIGHT = 65535
STEP = 500  # How much to change the brightness by each time

while True:
    # Fade In
    for brightness in range(OFF, MAX_BRIGHT, STEP):
        led.duty_cycle = brightness
        time.sleep(0.01)  # A tiny pause to make it smooth

    # Fade Out
    for brightness in range(MAX_BRIGHT, OFF, -STEP):
        led.duty_cycle = brightness
        time.sleep(0.01)