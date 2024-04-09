import librairie.py

sg90 = PWM(Pin(27, mode=Pin.OUT))
sg90.freq(50)
sg91 = PWM(Pin(12, mode=Pin.OUT))
sg91.freq(50)


# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88
i = 125
j = 0

def rotation (sg) :
    while i > 33 :
        sg.duty(i)
        time.sleep(0.01)
        i-= 1
        if i == 75 :
            time.sleep(2)
        if i == 33 :
            j = 1
            time.sleep(2)
    while j == 1 :
        sg.duty(i)
        time.sleep(0.01)
        i += 1
        if i == 75 :
            time.sleep(2)
        if i == 125 :
            j = 0
            time.sleep(2)


while True :
    rotation(sg90)
    rotation(sg91)