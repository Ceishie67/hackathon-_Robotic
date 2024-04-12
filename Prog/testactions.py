from machine import Pin,PWM
import time
from ankle import *
from hip import *
from knee import *

#cette fonction permet de faire avancer le robot pas a pas
def forward(nbstep) :


    #jambe gauche premier pas avec appuie jambe droite
    rotation_Lankle_half_neg_turn(0.01)
    #
    rotation_Rankle_half_pos_turn(0.01)
    #
    rotation_Lhip_half_neg_turn(0.01)
    #
    rotation_Rhip_half_neg_turn(0.01)
    #
    rotation_Lankle_return_neutral_neg(0.01)
    rotation_Lhip_return_neutral_neg(0.01)
    #
    rotation_Rhip_return_neutral_neg(0.01)
    rotation_Rankle_return_neutral_pos(0.01)
    
    #jambe gauche
    while nbstep > 0:

        rotation_Lankle_half_pos_turn()
        #
        rotation_Rankle_half_pos_turn()
        rotation_Rhip_half_pos_turn()
        #
        rotation_Lhip_half_pos_turn()
        #
        rotation_Rankle_return_neutral_pos()
        rotation_Rhip_return_neutral_pos()
        #
        rotation_Lhip_return_neutral_pos()
        rotation_Lankle_return_neutral_pos()

        # rotation_Rhip_half_neg_turn()
        # rotation_Rhip_return_neutral_neg()
        # #permet d'aligner le point de stablite et le centre de gravite
        # rotation_Rankle_half_neg_turn()
        # rotation_Rankle_return_neutral_neg()

        ######  deuxieme pas  ######
        
        rotation_Rankle_half_neg_turn()
        #
        rotation_Lankle_half_neg_turn()
        rotation_Lhip_half_neg_turn()
        #
        rotation_Rhip_half_neg_turn()
        #
        rotation_Lankle_return_neutral_neg()
        rotation_Lhip_return_neutral_neg()
        #
        rotation_Rhip_return_neutral_neg()
        rotation_Rankle_return_neutral_neg()
