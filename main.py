import time
from machine import Pin
import usb.device.keyboard


# Simple logger for MicroPython
def log_info(msg):
    t = time.ticks_ms()
    print('[INFO %dms] %s' % (t, msg))

# Raspberry Pi Pico W board pin configuration
BUTTON_PINS = [7, 8, 9, 19, 20, 21]  # 3x2 Layout

DEBOUNCE_MS = 20

# Button setup for Pico W
class DebouncedButton:
    
    def __init__(self, pin_num):
        self._pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self._last_state = self._pin.value()
        self._debounce_time = time.ticks_ms()

    def read(self):
        state = self._pin.value()
        now = time.ticks_ms()
        if state != self._last_state:
            self._debounce_time = now
            self._last_state = state
        if time.ticks_diff(now, self._debounce_time) > DEBOUNCE_MS:
            if self.stable_state != state:
                self.stable_state = state
        # Return 1 as long as button is held down (active low)
        return 1 if self.stable_state == 0 else 0


BUTTONS = [DebouncedButton(pin) for pin in BUTTON_PINS]

kbd = usb.device.keyboard.KeyboardInterface()

BUTTON_MAP = {
    0: (0x01, 0x3A),  # CTRL + F1
    1: (0x01, 0x3B),  # CTRL + F2
    2: (0x01, 0x3C),  # CTRL + F3
    3: (0x01, 0x3D),  # CTRL + F4
    4: (0x01, 0x3E),  # CTRL + F5
    5: (0x01, 0x3F),  # CTRL + F6
}


while True:
    states = []
    for i, btn in enumerate(BUTTONS):
        state = btn.pin.value()
        states.append(state)
        if btn.read() == 1:      # pressed
            kbd.send_keys(BUTTON_MAP[i])
            log_info('Button %d pressed: mods=%d, keycode=%d' % (i, BUTTON_MAP[i][0], BUTTON_MAP[i][1]))
    # log_info('Button states: %s' % states)
    time.sleep_ms(50)  # slightly longer delay for debug output
    