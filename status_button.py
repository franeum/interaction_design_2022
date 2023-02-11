from time import sleep
from machine import Pin

button = Pin(12, Pin.IN, Pin.PULL_UP)
previous_value = 1
DELAY = 0.01
ON = 0
OFF = 1

while True:
    new_value = button.value()
    
    # controllo che l'ultimo stato sia OFF
    # e che il precedente sia ON
    if new_value == ON and previous_value == OFF:
        print("bang")
        
    previous_value = new_value
    sleep(DELAY)
    