from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici ankle pour cheville
ankle = PWM(Pin(27, mode=Pin.OUT))
ankle.freq(50)

#position droite 77
#position min 45
#position max 120

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'avant
def rotation_ankle_half_pos_turn() :
    i = 77
        
    while i < 88 :
        time.sleep(0.2)
        ankle.duty(i)
        time.sleep(0.2)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'arriere
def rotation_ankle_half_neg_turn() :
    i = 87
    
    while i > 66 :
        time.sleep(0.2)
        ankle.duty(i)
        time.sleep(0.2)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre
def rotation_ankle_return_neutral() :
    i = 77
    ankle.duty(i)
    time.sleep(0.2)
    print(i)