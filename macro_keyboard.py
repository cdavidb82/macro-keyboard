# My Macro keyboard for Raspberry Pi Pic0
# written for MicroPython
# Reference: http://docs.micropython.org/en/latest/rp2/quickref.html

# This is a basic build or skeleton 
import machine
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
    while True:
        time.sleep(0.1) # wait for 100ms
        print('Waiting for key press...') # print a message to the console
        pass
