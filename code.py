import time
import board
import digitalio
from adafruit_debouncer import Debouncer

# Define keys
# Use appropriate board pin mapping
keys = [
    {"pin": board.GP6, "label": "A"},
    {"pin": board.GP7, "label": "B"},
    {"pin": board.GP8, "label": "C"},
    {"pin": board.GP9, "label": "D"},
    {"pin": board.GP10, "label": "E"},
    {"pin": board.GP18, "label": "F"},
    {"pin": board.GP19, "label": "G"},
    {"pin": board.GP20, "label": "H"},
    {"pin": board.GP21, "label": "I"},
    {"pin": board.GP22, "label": "J"},
]

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


# Set up keys with pull-up resistors
key_objects = []
for pin in keys:
    key = digitalio.DigitalInOut(pin["pin"])
    key.switch_to_input(pull=digitalio.Pull.UP)
    debouncer = Debouncer(key, 0.1)  # Debounce time in seconds
    key_objects.append(Key(debouncer, pin["label"]))


# Program Loop
if __name__ == "__main__":
    try:
        while True:
            for key in key_objects:
                key.update()
            time.sleep(0.01)  # wait for 10ms
    except KeyboardInterrupt:
        print('Program interrupted by user')
    finally:
        print('Program terminated')
