import librairie.py

sg90 = PWM(Pin(14, mode=Pin.OUT))
sg90.freq(50)
sg91 = PWM(Pin(12, mode=Pin.OUT))
sg91.freq(50)


# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

hankle_int = sg90.duty(65)
hankle_neut = sg90.duty(83)
hankle_ext = sg90.duty(133)

#knee
#knee
#knee

hip_front = sg91.duty(65)
hip_neut = sg91.duty(85)
hip_rear = sg91.duty(1359)

while True :
    hip_front
    time.sleep(1)
    hip_neut
    time.sleep(1)
    hip_rear
    time.sleep(1)
    