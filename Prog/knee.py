#-----------------------------------------------------------------------------#
# Fichier servant à initialiser et utiliser les servomoteurs de la hanche.
# Une structure de balisage est présente à travers ce code.
#   MEMO :
#       - K = Knee, sert de balisage pour les différentes fonctionnaliter.
#       - L = left, pour la différenciation entre les deux genoux.
#       - R = right, pour la différenciation entre les deux genoux.
#       - i = rotation du servomoteur présent servant de position de base.
#-----------------------------------------------------------------------------#


from machine import Pin,PWM
import time


###### ___START K1___ : Définition des Pins.

# Assignation des pins pour les moteurs de la hanche gauche.
Lknee = PWM(Pin(27, mode=Pin.OUT))
Lknee.freq(50)

#on definit le pin de la carte esp ici Rknee pour hanche
Rknee = PWM(Pin(35, mode=Pin.OUT))
Rknee.freq(50)

# position droite 77
# position min 35
# position max 115

###### ___END K1___


###### ___START K2___ : Définition des mouvements de base pour le genoux gauche.

# On defini une fonction qui permet au genoux de faire un mouvement vers l'avant.
def rotation_Lknee_half_pos_turn(tps) :
    i = 77
        
    while i < 88 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

# On defini une fonction qui permet au genoux de faire un mouvement vers l'arriere.
def rotation_Lknee_half_neg_turn(tps) :
    i = 87
    
    while i > 66 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
# On defini une fonction qui permet au genoux de faire un mouvement pour revenir en position neutre depuis la position arriere.
def rotation_Lknee_return_neutral_neg(tps) :
    i = 66
    while i < 77 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

# On defini une fonction qui permet au genoux de faire un mouvement pour revenir en position neutre depuis la position avant.
def rotation_Lknee_return_neutral_pos(tps) :
    i = 88
    while i > 77 :
        time.sleep(tps)
        Lknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'avant
def rotation_Rknee_half_pos_turn(tps) :
    i = 77
        
    while i < 88 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement vers l'arriere
def rotation_Rknee_half_neg_turn(tps) :
    i = 77
    while i > 50 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1

        
#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position arriere
def rotation_Rknee_return_neutral_neg(tps) :
    i = 50
    while i < 77 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i += 1

#on defini une fonction qui permet a la cheville de faire un mouvement pour revenir en position neutre depuis la position avant
def rotation_Rknee_return_neutral_pos(tps) :
    i = 88
    while i > 77 :
        time.sleep(tps)
        Rknee.duty(i)
        time.sleep(tps)
        print(i)
        i -= 1


