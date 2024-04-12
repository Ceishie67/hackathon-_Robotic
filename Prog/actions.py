from machine import Pin,PWM
import time
from ankle import *
from hip import *
from knee import *

#cette fonction permet de faire avancer le robot pas a pas
def forward(nbstep) :

    #jambe gauche
    while nbstep > 0:
        #permet de met
        rotation_Lankle_half_neg_turn()
        rotation_Lhip_half_neg_turn()
        rotation_Lankle_return_neutral_neg()
        rotation_Lhip_return_neutral_neg()
        nbstep -= 1

        rotation_Lhip_half_pos_turn()
        rotation_Lankle_half_pos_turn()
        rotation_Lhip_return_neutral_pos()
        rotation_Lhip_half_neg_turn()
        rotation_Lankle_return_neutral_pos()
        #permet d'aligner le point de stablite et le centre de gravite
        rotation_Lankle_half_neg_turn()
        rotation_Lhip_return_neutral_neg()
        rotation_Lankle_return_neutral_neg()
        nbstep -= 1