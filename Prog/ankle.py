from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici ankle pour cheville
ankle = PWM(Pin(12, mode=Pin.OUT))
ankle.freq(50)

#position droite 77
#position min 45
#position max 120

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'avant
def rotation_ankle_half_pos_turn() :
    i = 77
        
    while i < 88 :
        time.sleep(0.01)
        ankle.duty(i)
        time.sleep(0.01)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'arriere
def rotation_ankle_half_neg_turn() :
    i = 77
    while i > 50 :
        time.sleep(0.01)
        ankle.duty(i)
        time.sleep(0.01)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_ankle_return_neutral_neg() :
    i = 50
    while i < 77 :
        time.sleep(0.01)
        ankle.duty(i)
        time.sleep(0.01)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_ankle_return_neutral_pos() :
    i = 88
    while i > 77 :
        time.sleep(0.01)
        ankle.duty(i)
        time.sleep(0.01)
        print(i)
        i -= 1



