#---------------------------------------------------------#
# Fichier servant a lancer le programme en appelant les fonctions utiles a son bon fonctionnement
#---------------------------------------------------------#

from machine import Pin,PWM
import time
from ankle import *
from hip import *
from knee import *


# Permet de faire fonctionner le programme de toutes les fonctions importé en continue car la condition ne change jamais
while True:
    ankle.rotation_ankle_half_pos_turn()
    knee.rotation_knee_half_neg_turn()
    hip.rotation_hip_half_pos_turn()