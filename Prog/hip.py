from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici hip pour hanche
hip = PWM(Pin(12, mode=Pin.OUT))
hip.freq(50)

#position droite 77
#position min 45
#position max 110

#cette fonction permet a la hanche de faire un mouvement vers l'avant
def rotation_hip_half_pos_turn() :
    i = 77
        
    while i < 88 :
        time.sleep(0.2)
        hip.duty(i)
        time.sleep(0.2)
        print(i)
        i += 1

#cette fonction permet a la hanche de faire un mouvement vers l'arriere
def rotation_hip_half_neg_turn() :
    i = 87
    
    while i > 66 :
        time.sleep(0.2)
        hip.duty(i)
        time.sleep(0.2)
        print(i)
        i -= 1

        
#cette fonction permet a la hanche de faire un mouvement pour revenir en position neutre
def rotation_hip_return_neutral() :
    i = 77
    hip.duty(i)
    time.sleep(0.2)
    print(i)