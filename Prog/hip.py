from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici hip pour hanche
hip = PWM(Pin(26, mode=Pin.OUT))
hip.freq(50)

#position droite 77
#position min 45
#position max 110

#cette fonction permet a la hanche de faire un mouvement vers l'avant
def rotation_hip_half_pos_turn() :
    i = 77
        
    while i < 90 :
        time.sleep(0.01)
        hip.duty(i)
        time.sleep(0.01)
        print(i)
        i += 1

#cette fonction permet a la hanche de faire un mouvement vers l'arriere
def rotation_hip_half_neg_turn() :
    i = 77
    
    while i > 66 :
        time.sleep(0.01)
        hip.duty(i)
        time.sleep(0.01)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_hip_return_neutral_neg() :
    i = 66
    while i < 77 :
        time.sleep(0.01)
        hip.duty(i)
        time.sleep(0.01)
        print(i)
        i += 1

#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_hip_return_neutral_pos() :
    i = 90
    while i > 77 :
        time.sleep(0.01)
        hip.duty(i)
        time.sleep(0.01)
        print(i)
        i -= 1



