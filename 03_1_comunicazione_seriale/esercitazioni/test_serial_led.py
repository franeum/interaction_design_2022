import time
from machine import Pin

led = Pin(2, Pin.OUT)
speed = 1
light = 1

while True:
    led.value(light)
    msg = input()

    if msg:
        if msg == 'spegni':
            light = 0
        elif msg == 'accendi':
            light = 1

    print("stokazzo")
    time.sleep(speed)

