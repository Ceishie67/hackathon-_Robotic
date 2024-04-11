from librairie import *
from robot_legs import *

while True:
    sg90.duty(23)
    time.sleep(1)
    sg91.duty(25)
    time.sleep(1)
    sg90.duty(143)
    time.sleep(1)
    sg91.duty(123)
    time.sleep(1)