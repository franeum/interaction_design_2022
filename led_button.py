from time import sleep
from machine import Pin

led = Pin(2, Pin.OUT)
button = Pin(12, Pin.IN, Pin.PULL_UP)
previous_value = 1
DELAY = 0.01
ON = 0
OFF = 1
led_status = 0
counter = 0

while True:
    new_value = button.value()
    
    # controllo che l'ultimo stato sia OFF
    # e che il precedente sia ON
    if new_value == ON and previous_value == OFF:
        #print("bang")
        led_status = 1 - led_status
        led.value(led_status)
        
        if led_status == 1:
            print("acceso")
        else:
            print("spento")
            
        counter += 1
        print(counter)
        
    previous_value = new_value
    sleep(DELAY)
    