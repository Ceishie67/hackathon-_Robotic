from machine import Pin,PWM
import time

#sg90 = PWM(Pin(14, mode=Pin.OUT))
#sg90.freq(50)
#sg91 = PWM(Pin(12, mode=Pin.OUT))
#sg91.freq(50)
sg92 = PWM(Pin(14, mode=Pin.OUT))
sg92.freq(50)

# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

#hankle_int = sg90.duty(65)
#hankle_neut = sg90.duty(83)
#hankle_ext = sg90.duty(133)

#knee
#knee
#knee

#hip_front = sg91.duty(133)
#hip_neut = sg91.duty(80)
#hip_rear = sg91.duty(50)

while True :
    sg92.duty(120)
    print("un")
    time.sleep(2)
    sg92.duty(10)
    print("deux")
    time.sleep(2)
    sg92.duty(65)
    print("troix")
    time.sleep(2)
    

