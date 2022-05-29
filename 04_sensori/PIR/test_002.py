from naba_pir import PIR
import time

def fai(arg):
    print('bang')

pir = PIR(14, fai)
pir.calibrate()

while True:
    pir.operate()
    time.sleep(0.1)
