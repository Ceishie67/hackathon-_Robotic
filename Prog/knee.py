from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici knee pour genoux
knee = PWM(Pin(27, mode=Pin.OUT))
knee.freq(50)

#position droite 77
    #position min 35
    #position max 115

#cette fonction permet au genoux de faire un mouvement vers l'avant
def rotation_knee_half_pos_turn() :
    i = 77
        
    while i < 88 :
        time.sleep(0.01)
        knee.duty(i)
        time.sleep(0.01)
        print(i)
        i += 1

#cette fonction permet au genoux de faire un mouvement vers l'arriere
def rotation_knee_half_neg_turn() :
    i = 87
    
    while i > 66 :
        time.sleep(0.01)
        knee.duty(i)
        time.sleep(0.01)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_knee_return_neutral_neg() :
    i = 66
    while i < 77 :
        time.sleep(0.01)
        knee.duty(i)
        time.sleep(0.01)
        print(i)
        i += 1

#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_knee_return_neutral_pos() :
    i = 88
    while i > 77 :
        time.sleep(0.01)
        knee.duty(i)
        time.sleep(0.01)
        print(i)
        i -= 1

