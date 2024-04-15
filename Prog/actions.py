#-----------------------------------------------------------------------------#
# Fichier servant a definir les actions éxecutables pour creer un déplacement.
# Une structure de balisage est présente à travers ce code.
#   MEMO :
#       - Ac = Action, sert de balisage pour les différentes fonctionnaliter.
#       - neg = negative, donne le sens de rotation du servomoteur.
#       - pos = positive, donne le sens de rotation du servomoteur.
#       - L = left, pour la différenciation entre les deux membres.
#       - R = right, pour la différenciation entre les deux membres.
#-----------------------------------------------------------------------------#


from machine import Pin,PWM
import time
from ankle_back import *
from hip_back import *
from knee_back import *


###### ___START Ac1___ : Fonction pour faire avancer le robot, simulation de la marche.

# Fonction permettant de faire avancer le robot pas a pas.
def forward(nbstep) :

    #jambe gauche
    while nbstep > 0:
        rotation_Rankle_half_pos_turn(0.1)          # cheville droite ==> vers la gauche pour la stabilite
        #
        rotation_Lankle_half_neg_turn(0.1)          # cheville gauche ==> vers la gauche / debut du 1er mouvement
        #
        rotation_Lhip_half_neg_turn(0.1)            # hanche gauche ==> vers l'avant
        #
        rotation_Rhip_half_neg_turn(0.1)            # hanche droite / pied d'appuie ==> vers l'arriere / mouvement vers l'avant
        #
        rotation_Rankle_return_neutral_pos(0.1)     # retoure de la cheville droite en position neutre
        #
        rotation_Lankle_return_neutral_neg(0.1)     # retoure de la cheville gauche en position neutre / fin 1er mouvement
        rotation_Lankle_half_pos_turn(0.01)         # cheville gauche ==> vers la droite pour la stabilite
        #
        rotation_Rankle_half_neg_turn(0.01)         # cheville droite ==> vers la droite / debut du 2eme mouvement
        #
        rotation_Lhip_return_neutral_neg(0.01)      # retour de la hanche gauche en neutre
        #
        rotation_Rhip_return_neutral_neg(0.01)      # retour de la hanche droite en neutre
        rotation_Rhip_half_pos_turn(0.01)           # hanche droite ==> vers l'avant
        #
        rotation_Lhip_half_neg_turn(0.01)           # hanche gauche / pied d'appuie ==> vers l'arriere / mouvement vers l'avant
        #
        rotation_Lankle_return_neutral_pos(0.01)    # retoure de la cheville droite en position neutre
        rotation_Rankle_return_neutral_neg(0.01)    # retoure de la cheville gauche en position neutre / fin 2eme mouvement
        #
        rotation_Rhip_return_neutral_pos(0.01)      # retour de la hanche droite en neutre
        #
        rotation_Lhip_return_neutral_neg(0.01)      # retour de la hanche gauche en neutre / fin du mouvement vers l'avant
        #

###### ___END Ac1___


###### ___START Ac2___ : Fonction pour faire tourner le robot sur la gauche.

def left_turn() :
    rotation_Lankle_half_neg_turn(0.01)             # cheville gauche ==> vers la gauche
    
    # Rotation genoux gauche vers la gauche
    
    rotation_Lankle_return_neutral_neg(0.01)        # retour de la cheville gauche en neutre
    

###### ___END Ac2___
    

###### ___START Ac3___ : Fonction pour faire tourner le robot sur la droite.

def right_turn() :
    rotation_Rankle_half_neg_turn(0.01)             # cheville droite ==> vers la droite
    
    # Rotation genoux droit vers la droite
    
    rotation_Rankle_return_neutral_neg(0.01)        # retour de la cheville droite en neutre
    

###### ___END Ac3___


###### ___START Ac4___ : Fonction pour faire dancer le robot.

def lil_dance() :
    rotation_Rankle_half_pos_turn(0.001)            # cheville droite ==> vers la gauche pour la stabilite
    #
    rotation_Lankle_half_neg_turn(0.001)            # cheville gauche ==> vers la gauche
    #
    rotation_Rankle_return_neutral_pos(0.001)       # retoure de la cheville droite en position neutre
    #
    rotation_Lankle_return_neutral_neg(0.001)       # retoure de la cheville gauche en position neutre
    #
    rotation_Lankle_half_pos_turn(0.001)            # cheville gauche ==> vers la droite pour la stabilite
    #
    rotation_Rankle_half_neg_turn(0.001)            # cheville droite ==> vers la droite 
    #
    rotation_Lankle_return_neutral_pos(0.01)        # retoure de la cheville droite en position neutre
    #
    rotation_Rankle_return_neutral_neg(0.01)        # retoure de la cheville gauche en position neutre

###### ___END Ac4___


###### ___START Ac5___ : Fonction pour faire le grand écart, puis avancer et reculer la tête du robot.

def flex() :
    rotation_Lankle_half_neg_turn(0.001)
    #
    rotation_Rankle_half_neg_turn(0.001)
    #
    rotation_Rhip_half_neg_turn(0.001)
    #
    rotation_Lhip_half_pos_turn(0.001)
    #
    rotation_Lankle_return_neutral_pos()
    #
    rotation_Rhip_return_neutral_neg()
    #
    rotation_Rhip_half_pos_turn()
    #
    rotation_Lhip_half_neg_turn()
    #
    rotation_Lankle_return_neutral_neg()
    #
    rotation_Rhip_return_neutral_pos()
    #
    rotation_Lankle_return_neutral_neg()
    rotation_Rankle_return_neutral_neg()

    ###### ___END Ac5___
