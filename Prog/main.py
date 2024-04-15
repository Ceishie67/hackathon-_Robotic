#-----------------------------------------------------------------------------#
# Fichier servant a lancer le programme en appelant les fonctions utiles a son bon fonctionnement.
# Une structure de balisage est présente à travers ce code.
#   MEMO :
#       - M = Main, sert de balisage pour les différentes fonctionnaliter.
#       - neg = negative, donne le sens de rotation du servomoteur.
#       - pos = positive, donne le sens de rotation du servomoteur.
#-----------------------------------------------------------------------------#


from machine import Pin,PWM
import time
from actions import *
from ankle_back import *
from hip_back import *
from knee_back import *


###### ___START M1___ : Lancement des commandes executés par le robot.

# Permet de faire fonctionner le programme de toutes les fonctions importé en continue car la condition ne change jamais
while True:
    #forward(1)
    #
    rotation_Rankle_half_pos_turn(0.01)
    #
    rotation_Lankle_half_neg_turn(0.01)
    #
    rotation_Lhip_half_neg_turn(0.01)
    #
    rotation_Rhip_half_neg_turn(0.01)
    #
    rotation_Rankle_return_neutral_pos(0.01)
    rotation_Lankle_return_neutral_neg(0.01)
    rotation_Rankle_half_neg_turn(0.01)
    rotation_Lankle_half_pos_turn(0.01)
    #
    rotation_Lhip_return_neutral_neg(0.01)
    #
    rotation_Rhip_return_neutral_neg(0.01)
    #
    rotation_Rankle_return_neutral_neg(0.01)
    rotation_Lankle_return_neutral_pos(0.01)

###### ___END M1___
