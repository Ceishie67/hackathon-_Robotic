from machine import Pin,PWM
import time

#on definit le pin de la carte esp ici Lhip pour hanche
Lhip = PWM(Pin(26, mode=Pin.OUT))
Lhip.freq(50)

#on definit le pin de la carte esp ici Rhip pour hanche
Rhip = PWM(Pin(34, mode=Pin.OUT))
Rhip.freq(50)

#position droite 77
#position min 45
#position max 110

#cette fonction permet a la hanche de faire un mouvement vers l'avant
def rotation_Lhip_half_pos_turn(tps) :
    i = 77
        
    while i < 90 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#cette fonction permet a la hanche de faire un mouvement vers l'arriere
def rotation_Lhip_half_neg_turn(tps) :
    i = 77
    
    while i > 66 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Lhip_return_neutral_neg(tps) :
    i = 66
    while i < 77 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Lhip_return_neutral_pos(tps) :
    i = 90
    while i > 77 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'avant
def rotation_Rhip_half_pos_turn(tps) :
    i = 77
        
    while i < 88 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'arriere
def rotation_Rhip_half_neg_turn(tps) :
    i = 77
    while i > 50 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Rhip_return_neutral_neg(tps) :
    i = 50
    while i < 77 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Rhip_return_neutral_pos(tps) :
    i = 88
    while i > 77 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1


