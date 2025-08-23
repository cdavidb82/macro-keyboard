import time
from machine import Pin
import hid

# 4.1  Setup
DEBOUNCE_MS = 20
BUTTONS = [DebouncedButton(i) for i in range(10)]
encoder = Encoder(clk=10, dt=11, sw=12)

kbd = hid.keyboard.HIDKeyboard()

BUTTON_MAP = {
    0: 0x04,  # a
    1: 0x05,  # b
    2: 0x06,  # c
    3: 0x07,  # d
    4: 0x08,  # e
    5: 0x09,  # f
    6: 0x0A,  # g
    7: 0x0B,  # h
    8: 0x0C,  # i
    9: 0x0D,  # j
}


class Encoder:
    def __init__(self, clk, dt, sw=None):
        self.clk = Pin(clk, Pin.IN, Pin.PULL_UP)
        self.dt  = Pin(dt,  Pin.IN, Pin.PULL_UP)
        self.sw  = Pin(sw,  Pin.IN, Pin.PULL_UP) if sw else None
        self.last_state = self.clk.value() << 1 | self.dt.value()
        self.position = 0

    def poll(self):
        state = self.clk.value() << 1 | self.dt.value()
        if state != self.last_state:
            # 00->01 (CW) or 10->11 etc.
            diff = (state - self.last_state) & 0x03
            if diff == 1:          # CW
                self.position += 1
            elif diff == 3:        # CCW
                self.position -= 1
            self.last_state = state
        # optional push‑button
        if self.sw and self.sw.value() == 0:
            return 'click'
        return None




def send_key(keycode, mods=0):
    kbd.send(mods, keycode, 0)
    time.sleep_ms(10)
    kbd.send(0, 0, 0)


last_encoder_pos = encoder.position
while True:
    # Buttons
    for i, btn in enumerate(BUTTONS):
        if btn.read() == 1:      # pressed
            send_key(BUTTON_MAP[i])

    # Encoder rotation
    pos = encoder.position
    if pos != last_encoder_pos:
        delta = pos - last_encoder_pos
        if delta > 0:
            # Rotate CW → send "Page Up" (0x3A)
            send_key(0x3A)
        else:
            # Rotate CCW → send "Page Down" (0x3B)
            send_key(0x3B)
        last_encoder_pos = pos

    # Encoder click (optional)
    click = encoder.poll()
    if click == 'click':
        send_key(0x28)  # ENTER

    time.sleep_ms(5)  # small delay to reduce CPU usage
