import time
from machine import Pin

led = Pin(2, Pin.OUT)
state = 0

while True:
    state = 1 - state
    print('bang')
    led.value(state)

    time.sleep(1)

