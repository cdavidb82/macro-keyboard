# My Macro keyboard for Raspberry Pi Pico
# written for MicroPython
# Reference: http://docs.micropython.org/en/latest/rp2/quickref.html
# Reference: https://github.com/raspberrypi/pico-sdk/blob/master/documentation/boards
#            /rp2040/README.md


# This is a basic build or skeleton 

import time
from machine import Pin # type: ignore
from machine import Timer # type: ignore

# Define keys
KEY_A = 20
KEY_B = 21

# Map keys to GPIO pins
key_a_pin = Pin(KEY_A, Pin.IN, Pin.PULL_UP)
key_b_pin = Pin(KEY_B, Pin.IN, Pin.PULL_UP)

class Key:
    def __init__(self, pin, name):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.name = name
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.key_pressed)
        self.pressed = False

    def key_pressed(self, pin):
        if not self.pressed:
            print(f'Key pressed: {self.name}')
            self.pressed = True
        else:
            print(f'Key released: {self.name}')
            self.pressed = False

# Create key objects
key_a = Key(KEY_A, 'A')
key_b = Key(KEY_B, 'B')

# Program Loop
if __name__ == "__main__":
    try:
        while True:
            time.sleep(0.1) # wait for 100ms
    except KeyboardInterrupt:
        print('Program interrupted by user')
    finally:
        key_a.pin.irq(trigger=0, handler=None)
        key_b.pin.irq(trigger=0, handler=None)
        print('Program terminated')