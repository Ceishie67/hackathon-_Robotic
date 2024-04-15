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
from ankle import *
from hip import *
from knee import *


###### ___START M1___ : Lancement des commandes executés par le robot.

# Permet de faire fonctionner le programme de toutes les fonctions importé en continue car la condition ne change jamais
while True:
    #forward(1)
    #
    rotation_Rankle_half_pos_turn(0.01) # cheville droite ==> vers la gauche pour la stabilite
    #
    rotation_Lankle_half_neg_turn(0.01) # cheville gauche ==> vers la gauche / debut du 1er mouvement
    #
    rotation_Lhip_half_neg_turn(0.01) # hanche gauche ==> vers l'avant
    #
    rotation_Rhip_half_neg_turn(0.01) # hanche droite / pied d'appuie ==> vers l'arriere / mouvement vers l'avant
    #
    rotation_Lankle_return_neutral_neg(0.01) # retoure de la cheville gauche en position neutre
    #
    rotation_Rankle_return_neutral_pos(0.01) # retoure de la cheville droite en position neutre
    #
    rotation_Rhip_return_neutral_neg(0.01) # retour de la hanche droite en neutre
    #
    rotation_Lhip_return_neutral_neg(0.01) # retour de la hanche gauche en neutre/ fin 1er mouvement
    #
    rotation_Lankle_half_pos_turn(0.01) # cheville gauche ==> vers la droite pour la stabilite
    #
    rotation_Rankle_half_neg_turn(0.01) # cheville droite ==> vers la droite / debut du 2eme mouvement
    #
    rotation_Rhip_half_pos_turn(0.01) # hanche droite ==> vers l'avant
    #
    rotation_Lhip_half_pos_turn(0.01) # hanche gauche / pied d'appuie ==> vers l'arriere / mouvement vers l'avant
    #
    rotation_Rankle_return_neutral_neg(0.01) # retoure de la cheville gauche en position neutre 
    rotation_Lankle_return_neutral_pos(0.01) # retoure de la cheville droite en position neutre / fin 2eme mouvement
    #
    rotation_Rhip_return_neutral_pos(0.01) # retour de la hanche droite en neutre
    #
    rotation_Lhip_return_neutral_pos(0.01) # retour de la hanche gauche en neutre / fin du mouvement vers l'avant
    #

###### ___END M1___
