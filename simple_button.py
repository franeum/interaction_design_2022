from machine import Pin
from time import sleep

DELAY = 0.1
button = Pin(12, Pin.IN)
led = Pin(2, Pin.OUT)

while True:
    val = button.value()
    print(val)
    led.value(1 - val)
    sleep(DELAY)

