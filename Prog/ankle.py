from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici Lankle pour cheville gauche
Lankle = PWM(Pin(12, mode=Pin.OUT))
Lankle.freq(50)

#on definit le pin de la carte esp ici Lankle pour cheville droite
Rankle = PWM(Pin(2, mode=Pin.OUT))
Rankle.freq(50)

#position droite 77
#position min 45
#position max 120

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'avant
def rotation_Lankle_half_pos_turn(tps) :
    i = 77
        
    while i < 95 :
        time.sleep(tps)
        Lankle.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'arriere
def rotation_Lankle_half_neg_turn(tps) :
    i = 77
    while i > 50 :
        time.sleep(tps)
        Lankle.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Lankle_return_neutral_neg(tps) :
    i = 50
    while i < 77 :
        time.sleep(tps)
        Lankle.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Lankle_return_neutral_pos(tps) :
    i = 88
    while i > 77 :
        time.sleep(tps)
        Lankle.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1


#on defini une fonction qui permet a la cheville de faire un mouvement vers l'avant
def rotation_Rankle_half_pos_turn(tps) :
    i = 50
        
    while i < 67 :
        time.sleep(tps)
        Rankle.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'arriere
def rotation_Rankle_half_neg_turn(tps) :
    i = 50
    while i > 20 :
        time.sleep(tps)
        Rankle.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Rankle_return_neutral_neg(tps) :
    i = 20
    while i < 50 :
        time.sleep(tps)
        Rankle.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Rankle_return_neutral_pos(tps) :
    i = 67
    while i > 50 :
        time.sleep(tps)
        Rankle.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1





