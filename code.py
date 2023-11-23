# Code for Macro Keyboard with CircuitPy

import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define keypad matrix
keypad_rows = [board.GP2, board.GP3, board.GP4, board.GP5]
keypad_cols = [board.GP6, board.GP7, board.GP8, board.GP9]

# Initialize Keyboard
keyboard = Keyboard

# Define keycodes for each button (adjust as needed)
keycodes = (
    [Keycode.A, Keycode.B, Keycode.C, Keycode.D],
    [Keycode.E, Keycode.F, Keycode.G, Keycode.H]
)


# Function to execute when a button is pressed
def execute_macro(row, col):
    keycode = keycodes[row][col]
    keyboard.press(keycode)
    time.sleep(0.1)  # adjust as needed
    keyboard.release_all()


# Main Loop
def main():
    while True:
        for row in range(4):
            for col in range(4):
                if not digitalio.DigitalInOut(keypad_cols[col]).value:
                    execute_macro(row, col)
                    time.sleep(0.2)  # Adjust as needed.


if __name__ == "__main__":
    main()
