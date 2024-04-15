from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici Lknee pour genoux
Lknee = PWM(Pin(27, mode=Pin.OUT))
Lknee.freq(50)

#on definit le pin de la carte esp ici Rknee pour hanche
Rknee = PWM(Pin(19, mode=Pin.OUT))
Rknee.freq(50)

#position droite 77
    #position min 35
    #position max 115

#cette fonction permet au genoux de faire un mouvement vers l'avant
def rotation_Lknee_half_pos_turn(tps) :
    i = 77
        
    while i < 88 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#cette fonction permet au genoux de faire un mouvement vers l'arriere
def rotation_Lknee_half_neg_turn(tps) :
    i = 87
    
    while i > 66 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Lknee_return_neutral_neg(tps) :
    i = 66
    while i < 77 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Lknee_return_neutral_pos(tps) :
    i = 88
    while i > 77 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

#on defini une fonction qui permet a la genoux de faire un mouvement vers l'avant
def rotation_Rknee_half_pos_turn(tps) :
    i = 77
        
    while i < 88 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la genoux de faire un mouvement vers l'arriere
def rotation_Rknee_half_neg_turn(tps) :
    i = 77
    while i > 50 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la genoux de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Rknee_return_neutral_neg(tps) :
    i = 50
    while i < 77 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la genoux de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Rknee_return_neutral_pos(tps) :
    i = 88
    while i > 77 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1
