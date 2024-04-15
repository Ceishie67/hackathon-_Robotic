#-----------------------------------------------------------------------------#
# Fichier servant à initialiser et utiliser les servomoteurs de la hanche.
# Une structure de balisage est présente à travers ce code.
#   MEMO :
#       - Hi = Hip, sert de balisage pour les différentes fonctionnaliter.
#       - L = left, pour la différenciation entre les deux hanches.
#       - R = right, pour la différenciation entre les deux hanches.
#       - i = rotation du servomoteur présent servant de position de base.
#-----------------------------------------------------------------------------#


from machine import Pin,PWM
import time


###### ___START Hi1___ : Définition des Pins.

# Assignation des pins pour les moteurs de la hanche gauche.
Lhip = PWM(Pin(26, mode=Pin.OUT))
Lhip.freq(50)

# Assignation des pins pour les moteurs de la hanche droite.
Rhip = PWM(Pin(34, mode=Pin.OUT))
Rhip.freq(50)

# position droite 77
# position min 45
# position max 110

###### ___END Hi1___


###### ___START Hi2___ : Définition des mouvements de base pour la hanche gauche.

# On defini une fonction qui permet a la hanche de faire un mouvement vers l'avant.
def rotation_Lhip_half_pos_turn(tps) :
    i = 77
        
    while i < 90 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

# On defini une fonction qui permet a la hanche de faire un mouvement vers l'arriere.
def rotation_Lhip_half_neg_turn(tps) :
    i = 77
    
    while i > 50 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
# On defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position arriere.
def rotation_Lhip_return_neutral_neg(tps) :
    i = 50
    while i < 77 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

# On defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position avant.
def rotation_Lhip_return_neutral_pos(tps) :
    i = 90
    while i > 77 :
        time.sleep(tps)
        Lhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

###### ___END Hi2___
        

###### ___START Hi3___ : Définition des mouvements de base pour la hanche droite.

# On defini une fonction qui permet a la hanche de faire un mouvement vers l'avant.
def rotation_Rhip_half_pos_turn(tps) :
    i = 77
        
    while i < 120 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

# On defini une fonction qui permet a la hanche de faire un mouvement vers l'arriere.
def rotation_Rhip_half_neg_turn(tps) :
    i = 77
    while i > 50 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
# On defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position arriere.
def rotation_Rhip_return_neutral_neg(tps) :
    i = 50
    while i < 77 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

# On defini une fonction qui permet a la hanche de faire un mouvement pour revenir en position neutre depuis la position avant.
def rotation_Rhip_return_neutral_pos(tps) :
    i = 120
    while i > 77 :
        time.sleep(tps)
        Rhip.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

###### ___END Hi3___
