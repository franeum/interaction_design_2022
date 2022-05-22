#!/usr/bin/env python3

"""
import sys
import select
import time
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(1)

ch = None

while True:
    time.sleep(0.1)

    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        ch = sys.stdin.read(1)
        #print(ch)

    if ch:
        if ch == 1:
            led.value(1)
        elif ch == 0:
            led.value(0)

    #print("prove it doesn't block")
"""

import sys, select
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(1)

i, o, e = select.select( [sys.stdin], [], [], 10 )

if (i):
    try:
        val = int(sys.stdin.readline().strip())
        led.value(0)
    except:
        pass
else:
    pass
