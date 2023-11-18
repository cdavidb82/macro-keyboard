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
def open_terminal(): # open terminal windows in Linux/macOS
    keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
    keyboard.release_all()

# Placeholder for now.
def run_script_a():
    pass

# Cycle keycodes for keys pressed. 
while True:
    for i in range(10):
        if not buttons[i].value:
            # Button is pressed
            if i == 0:
                open_terminal()
            elif i == 1:
                run_script_a()
            # elif i == 2:
            #     run_script_a() 
            # TODO: Add for each keycode.
                
            time.sleep(0.1) # adjust as needed. 
