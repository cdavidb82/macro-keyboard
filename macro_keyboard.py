# My Macro keyboard for Raspberry Pi Pico
# written for MicroPython
# Reference: http://docs.micropython.org/en/latest/rp2/quickref.html
# Reference: https://github.com/raspberrypi/pico-sdk/blob/master/documentation/boards
#            /rp2040/README.md


# This is a basic build or skeleton 

import time
from machine import Pin
from machine import Timer

# Define keys
KEY_A = 20
KEY_B = 21

# Map keys to GPIO pins
key_a_pin = Pin(KEY_A, Pin.IN, Pin.PULL_UP)
key_b_pin = Pin(KEY_B, Pin.IN, Pin.PULL_UP)

def key_pressed(pin):
    print(f'Key pressed on pin:{pin}')

# Attach interrupt handlers to keys
key_a_pin.irq(trigger=Pin.IRQ_FALLING, handler=lambda p: key_pressed(KEY_A))
key_b_pin.irq(trigger=Pin.IRQ_FALLING, handler=lambda p: key_pressed(KEY_B))

# Program Loop
if __name__ == "__main__":
    try:
        while True:
            time.sleep(0.1) # wait for 100ms
    except KeyboardInterrupt:
        print('Program interrupted by user')
    finally:
        key_a_pin.irq(trigger=0, handler=None)
        key_b_pin.irq(trigger=0, handler=None)
        print('Program terminated')
