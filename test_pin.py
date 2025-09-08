# This script is for testing PIN.IN, Pin.PULL_UP values to specific pins on the Pico_W


import time
from machine import Pin

TEST_PIN = 7  # Change to the pin you want to test

while True:
    val = Pin(TEST_PIN, Pin.IN, Pin.PULL_UP).value()
    print('Pin %d value: %d' % (TEST_PIN, val))
    time.sleep_ms(100)
