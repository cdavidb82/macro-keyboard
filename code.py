# Code for Macro Keyboard with CircuitPy

import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define button pins
button_pins = [board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.D10, board.D11]

# Intialize buttons
buttons = [DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = Direction.INPUT
    button.pull = Pull.UP

# Initialize Keyboard
keyboard = Keyboard()

# Define keycodes (adjust as needed)
keycodes = [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F, Keycode.G, Keycode.H, Keycode.I, Keycode.J]

while True:
    for i in range(10):
        if not buttons[i].value:
            # Button is pressed
            keyboard.press(keycodes[i])
            time.sleep(0.1) # adjust as needed
            keyboard.release_all()
            time.sleep(0.1) # adust as needed
