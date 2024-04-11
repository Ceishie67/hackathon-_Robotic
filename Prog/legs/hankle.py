from machine import Pin,PWM
import time

def rotation_hankle_half_pos_turn() :
    sg90 = PWM(Pin(12, mode=Pin.OUT))
    sg90.freq(50)
    i = 125

    while i > 33 :
        sg90.duty(i)
        time.sleep(0.01)
        i -= 1