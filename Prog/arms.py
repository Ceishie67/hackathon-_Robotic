#-----------------------------------------------------------------------------#
# Fichier servant à initialiser et utiliser les servomoteurs du bras.
# Une structure de balisage est présente à travers ce code.
#   MEMO :
#       - A = Arms, sert de balisage pour les différentes fonctionnaliter.
#       - L = left, pour la différenciation entre les deux bras.
#       - R = right, pour la différenciation entre les deux bras.
#       - rotation = rotation du servomoteur présent servant de position de base.
#-----------------------------------------------------------------------------#


from machine import Pin,PWM
import time


###### ___START A1___ : Définition des Pins.

# Assignation des pins pour les moteurs des bras.
armsR = PWM(Pin(2, mode=Pin.OUT))       # create PWM object from a pin
armsR.freq(50)                          # set PWM frequency from 50Hz
armsL = PWM(Pin(4, mode=Pin.OUT))
armsL.freq(50)

###### ___END A1___


###### ___START A2___ : Définition des mouvements de base pour le bras.

# Positionnement du bras gauche horizontalement.
def rotation_arms_lft_pos_turn():
    rotation = 42
    while rotation < 90 :
        armsL.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation += 1

# Positionnement du bras gauche verticalement vers le haut.
def rotation_arms_lft_pos_turn_hight():
    rotation = 90
    while rotation < 120 :
        armsL.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation += 1

# Positionnement du bras droit horizontalement.
def rotation_arms_rgt_pos_turn():
    rotation = 130
    while rotation > 85 :
        armsR.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation -= 1

# Positionnement du bras droit verticalement vers le haut.
def rotation_arms_rgt_pos_turn_hight():
    rotation = 85
    while rotation > 42 :
        armsR.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation -= 1

###### ___END A2___
        

###### ___START A3___ : Création d'un mouvement pour saluer.
        
# Création d'un mouvement où le bras varie légèrement de bas en haut avec une position de base horizontale.
def hello_arms_turn():
    rotation = 80
    while rotation < 105 :
        armsL.duty(rotation)
        time.sleep(0.01)
        print(rotation)
        rotation += 1
        while rotation > 80 :
            armsL.duty(rotation)
            time.sleep(0.01)
            print(rotation)
            rotation -= 1

###### ___END A3___


###### ___START A4___ : Création d'un mouvement pour célébrer.
            
# Création d'un mouvement des bras simultanément en position verticale haute.
def hourra_arms_turn():
    rotationR = 60
    rotationL = 115
    while rotationR > 42 :
        armsR.duty(rotationR)
        armsL.duty(rotationL)
        time.sleep(0.03)
        print(rotationR,rotationL)
        rotationL += 1
        rotationR -= 1

###### ___END A4___
        

###### ___START A5___ : Création d'un mouvement pour faire une ola.
        
# Création d'un mouvement pour lever les bras simultanément de bas en haut.
def ola():
    time.sleep(1)
    rotationR = 105
    y = 70
    while rotationR > 45 :
        armsR.duty(rotationR)
        armsL.duty(rotationL)
        time.sleep(0.02)
        print(rotationR,rotationL)
        rotationL += 1
        rotationR -= 1

###### ___END A5___
