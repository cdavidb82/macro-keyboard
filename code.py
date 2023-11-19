# Code for Macro Keyboard with CircuitPy

import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define keypad matrix
keypad_rows = [board.GP2, board.GP3, board.GP4, board.GP5 ]
keypad_cols = [board.GP6, board.GP7, board.GP8, board.GP9]

# Create the keypad object
keys = [
    [digitalio.DigitalInOut(pin) for pin in keypad_cols],
    [digitalio.DigitalInOut(pin) for pin in keypad_rows]
]
for row in keys:
    for key in row:
        key.direction = digitalio.Direction.INPUT
        key.pull = digitalio.Pull.UP

# Initialize Keyboard
keyboard = Keyboard()

# Define keycodes for each button (adjust as needed)
keycodes = [
    [Keycode.A, Keycode.B, Keycode.C, Keycode.D],
    [Keycode.E, Keycode.F, Keycode.G, Keycode.H],
    [Keycode.I, Keycode.J, Keycode.K, Keycode.L],
    [Keycode.M, Keycode.N, Keycode.O, Keycode.P]
]

# Function to exexcute when a button is pressed
def execute_macro(row, col):
    keycode = keycodes[row][col]
    keyboard.press(keycode)
    time.sleep(0.1) # adjust as needed
    keyboard.release_all()

# Main Loop
while True:
    for row in range(4):
        for col in range(4):
            if not keys[row][col].value:
                execute_macro(row, col)
                time.sleep(0.2) # Adjust as needed. 