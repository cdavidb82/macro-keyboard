import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


# Simple logger for MicroPython
def log_info(msg):
    t = int(time.monotonic() * 1000)
    print('[INFO %dms] %s' % (t, msg))

# Button pin configuration (change as needed)
BUTTON_PINS = [board.GP7, board.GP8, board.GP9, board.GP19, board.GP20, board.GP21]

DEBOUNCE_MS = 50

# Set up buttons with pull-ups
buttons = []
for pin in BUTTON_PINS:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

kbd = Keyboard(usb_hid.devices)

# Map button index to key combos
BUTTON_MAP = {
    0: [Keycode.CONTROL, Keycode.F1],
    1: [Keycode.CONTROL, Keycode.F2],
    2: [Keycode.CONTROL, Keycode.F3],
    3: [Keycode.CONTROL, Keycode.F4],
    4: [Keycode.CONTROL, Keycode.F5],
    5: [Keycode.CONTROL, Keycode.F6],
}

prev_states = [True] * len(buttons)  # True means not pressed (pull-up)

while True:
    for i, btn in enumerate(buttons):
        pressed = not btn.value  # Active low
        if pressed and prev_states[i]:
            kbd.press(*BUTTON_MAP[i])
            log_info('Button %d pressed: mods=%d, keycode=%d' % (i, BUTTON_MAP[i][0], BUTTON_MAP[i][1]))
        elif not pressed and not prev_states[i]:
            kbd.release(*BUTTON_MAP[i])
            log_info('Button %d released: mods=%d, keycode=%d' % (i, BUTTON_MAP[i][0], BUTTON_MAP[i][1]))
        prev_states[i] = pressed
    time.sleep(DEBOUNCE_MS / 1000)
