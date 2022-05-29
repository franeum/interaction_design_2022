import time
from machine import Pin
from naba_pir import PIR

def action(v):
    print(v)

pir = PIR(14, action)
led = Pin(2, Pin.OUT)

pir.calibrate()

while True:
    pir.operate()
    time.sleep(0.02)
