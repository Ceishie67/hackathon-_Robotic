from machine import Pin,PWM
import time

#assignation des pin pour moteur robot des bras. L = left R = right.
armsR = PWM(Pin(2, mode=Pin.OUT))
armsR.freq(50)
armsL = PWM(Pin(4, mode=Pin.OUT))
armsL.freq(50)

#les i present servent de position de base.

#fonction crée pour positionner le bras gauche en angle droit.
def rotation_arms_lft_pos_turn():
    rotation = 42
    while rotation < 90 :
        armsL.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation += 1
#fonction crée pour positionner le bras gauche haut.       
def rotation_arms_lft_pos_turn_hight():
    rotation = 90
    while rotation < 120 :
        armsL.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation += 1
        
#fonction permetant un movement haut bas servant a saluer.       
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
#fonction crée pour positionner le bras droit en angle droit.
def rotation_arms_rgt_pos_turn():
    rotation = 130
    while rotation > 85 :
        armsR.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation -= 1
#fonction crée pour positionner le bras droit en haut.       
def rotation_arms_rgt_pos_turn_hight():
    rotation = 85
    while rotation > 42 :
        armsR.duty(rotation)
        time.sleep(0.03)
        print(rotation)
        rotation -= 1
#fonction crée pour célébrer une victoire. crée un mouvement des bras simultanément en position haute.
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
        
#fonction crée pour célébrer une victoire. permet de lever les bras simultanément de bas en haut.
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
