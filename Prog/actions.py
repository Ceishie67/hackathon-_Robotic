from machine import Pin,PWM
import time
from ankle import *
from hip import *
from knee import *

#cette fonction permet de faire avancer le robot pas a pas
def forward(nbstep) :

    #jambe gauche
    while nbstep > 0:
        rotation_hip_half_pos_turn()
        rotation_ankle_half_neg_turn()
        rotation_hip_return_neutral_pos()
        rotation_hip_half_neg_turn()
        rotation_ankle_return_neutral_neg()
        rotation_ankle_half_pos_turn()
        rotation_hip_return_neutral_neg()
        #permet d'aligner le point de stablite et le centre de gravite
        rotation_ankle_return_neutral_pos()
        nbstep -= 1

        rotation_hip_half_pos_turn()
        rotation_ankle_half_pos_turn()
        rotation_hip_return_neutral_pos()
        rotation_hip_half_neg_turn()
        rotation_ankle_return_neutral_neg()
        rotation_ankle_half_pos_turn()
        rotation_hip_return_neutral_neg()
        #permet d'aligner le point de stablite et le centre de gravite
        rotation_ankle_return_neutral_pos()


        nbstep -= 1