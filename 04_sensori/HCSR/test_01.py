from hcsr04 import SR04
import time

SR = SR04(13, 14)

time.sleep_ms(2000)
_sum = [0] * 16
_previous = 0
counter = 0

while True:
    _sum[counter] = SR.distanceCM()
    counter += 1
    if counter > 15:
        counter = 0

    _avg = int(sum(_sum) / 16)

    if _avg != _previous:
        print(_avg)
        _previous = _avg

    time.sleep_ms(50)
