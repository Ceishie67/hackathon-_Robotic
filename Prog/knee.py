from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici hip pour genoux
knee = PWM(Pin(26, mode=Pin.OUT))
knee.freq(50)

#position droite 77
    #position min 35
    #position max 115

#cette fonction permet au genoux de faire un mouvement vers l'avant
def rotation_knee_half_pos_turn() :
    i = 77
        
    while i < 88 :
        time.sleep(0.2)
        knee.duty(i)
        time.sleep(0.2)
        print(i)
        i += 1

#cette fonction permet au genoux de faire un mouvement vers l'arriere
def rotation_knee_half_neg_turn() :
    i = 87
    
    while i > 66 :
        time.sleep(0.2)
        knee.duty(i)
        time.sleep(0.2)
        print(i)
        i -= 1

        
#cette fonction permet au genoux de faire un mouvement pour revenir en position neutre
def rotation_knee_return_neutral() :
    i = 77
    knee.duty(i)
    time.sleep(0.2)
    print(i)