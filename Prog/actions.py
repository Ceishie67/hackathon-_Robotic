from machine import Pin,PWM
import time
from ankle import *
from hip import *
from knee import *

#cette fonction permet de faire avancer le robot pas a pas
def forward(nbstep) :

    #jambe gauche
    while nbstep > 0:
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



def left_turn() :
    rotation_Lankle_half_neg_turn(0.01) # cheville gauche ==> vers la gauche
    #
    # rotation genoux gauche vers la gauche
    #
    rotation_Lankle_return_neutral_neg(0.01) # retour de la cheville gauche en neutre
    #


def right_turn() :
    rotation_Rankle_half_neg_turn(0.01) # cheville droite ==> vers la droite
    #
    # rotation genoux droit vers la droite
    #
    rotation_Rankle_return_neutral_neg(0.01) # retour de la cheville droite en neutre
    #

def lil_dance() :
    rotation_Rankle_half_pos_turn(0.001) # cheville droite ==> vers la gauche pour la stabilite
    #
    rotation_Lankle_half_neg_turn(0.001) # cheville gauche ==> vers la gauche
    #
    rotation_Rankle_return_neutral_pos(0.001) # retoure de la cheville droite en position neutre
    #
    rotation_Lankle_return_neutral_neg(0.001) # retoure de la cheville gauche en position neutre
    #
    rotation_Lankle_half_pos_turn(0.001) # cheville gauche ==> vers la droite pour la stabilite
    #
    rotation_Rankle_half_neg_turn(0.001) # cheville droite ==> vers la droite 
    #
    rotation_Lankle_return_neutral_pos(0.01) # retoure de la cheville droite en position neutre
    #
    rotation_Rankle_return_neutral_neg(0.01) # retoure de la cheville gauche en position neutre

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