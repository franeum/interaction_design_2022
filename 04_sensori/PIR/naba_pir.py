import time
import random
from machine import Pin

class PIR:
    CALTIME = 30

    def __init__(self, pin=None, callback=None, debug=1):
        self._sensor = Pin(pin, Pin.IN)
        self._previous = 0
        self._current = 0
        self._callback = callback
        self._debug = debug

    def calibrate(self):
        caltime = self.CALTIME
        while caltime:
            caltime -= 1
            if self._debug:
                print(caltime)
            time.sleep(1)

        if self._debug:
            print('end calibration, PIR now active')

    def operate(self):
        current = self._sensor.value()
        if current == 1 and current != self._previous:
            if self._debug:
                print(f"DEBUG: {random.randint(0,65535)}")
            self._callback(current)

        elif current == 0 and current != self._previous:
            if self._debug:
                print("DEBUG: NEWLY READY TO SENSE")
        self._previous = current

