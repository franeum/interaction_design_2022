from machine import Pin
import time

led = Pin(2, Pin.OUT)
push = Pin(13, Pin.IN)

while True:
    push_value = push.value()
    if push_value == 1:
        # spegni il led
        led.value(0)
    else:
        # accendi il led
        led.value(1)

    time.sleep(0.5)
