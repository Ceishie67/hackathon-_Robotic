from machine import Pin,PWM
import time


def rigth_leg() :
sg90 = PWM(Pin(14, mode=Pin.OUT))
sg90.freq(50)
sg91 = PWM(Pin(12, mode=Pin.OUT))
sg91.freq(50)


# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

while True:
    sg90.duty(23)
    time.sleep(1)
    sg91.duty(25)
    time.sleep(1)
    sg90.duty(143)
    time.sleep(1)
    sg91.duty(123)
    time.sleep(1)