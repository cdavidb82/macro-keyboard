import time
import board
import digitalio
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
        elif self.debouncer.rose:
            if self.pressed:
                print(f'Key released: {self.name}')
                self.pressed = False

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