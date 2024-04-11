import Prog.library as library
import Prog.library as library

def rotation() :

    sg90 = PWM(Pin(27, mode=Pin.OUT))
    sg90.freq(50)
    sg91 = PWM(Pin(12, mode=Pin.OUT))
    sg91.freq(50)
    i = 125
    j = 0

    
    while i > 33 :
        sg90.duty(i)
        time.sleep(0.01)
        i -= 1
        if i == 75 :
            time.sleep(2)
        if i == 33 :
            j = 1
            time.sleep(2)
    while j == 1 :
        sg90.duty(i)
        time.sleep(0.01)
        i += 1
        if i == 75 :
            time.sleep(2)
        if i == 125 :
            j = 0
            time.sleep(2)


while True :
    rotation()
