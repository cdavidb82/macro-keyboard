import os
import time
import board
import digitalio
import displayio
from adafruit_debouncer import Debouncer

# Define keys
KEY_A = board.GP20  # Use appropriate board pin mapping
KEY_B = board.GP21  # Use appropriate board pin mapping

# Set up keys with pull-up resistors
key_a_pin = digitalio.DigitalInOut(KEY_A)
key_a_pin.direction = digitalio.Direction.INPUT
key_a_pin.pull = digitalio.Pull.UP

key_b_pin = digitalio.DigitalInOut(KEY_B)
key_b_pin.direction = digitalio.Direction.INPUT
key_b_pin.pull = digitalio.Pull.UP

# Debouncer for key presses
key_a_debouncer = Debouncer(key_a_pin)
key_b_debouncer = Debouncer(key_b_pin)

#TODO: Create functions when key is pressed. Either by passing arguments or controls

# Define functions to handle key press events
def on_key_a_pressed():
    print("Function for Key A pressed")

def on_key_b_pressed():
    print("Function for Key B pressed")

# Define functions to handle key release events
def on_key_a_released():
    print("Function for Key A released")

def on_key_b_released():
    print("Function for Key B released")

class Key:
    def __init__(self, debouncer, name):
        self.debouncer = debouncer
        self.name = name
        self.pressed = False

    def update(self):
        self.debouncer.update()
        if self.debouncer.fell:
            if not self.pressed:
                print(f'Key pressed: {self.name}')
                self.pressed = True
                if self.name == 'A':
                    on_key_a_pressed()
                elif self.name == 'B':
                    on_key_b_pressed()
        elif self.debouncer.rose:
            if self.pressed:
                print(f'Key released: {self.name}')
                self.pressed = False
                if self.name == 'A':
                    on_key_a_released()
                elif self.name == 'B':
                    on_key_b_released()

# Create key objects
key_a = Key(key_a_debouncer, 'A')
key_b = Key(key_b_debouncer, 'B')

# Program Loop
if __name__ == "__main__":
    try:
        while True:
            key_a.update()
            key_b.update()
            time.sleep(0.01)  # wait for 10ms
    except KeyboardInterrupt:
        print('Program interrupted by user')
    finally:
        print('Program terminated')