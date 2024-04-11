#---------------------------------------------------------#
# Fichier servant a lancer le programme en appelant les fonctions utiles a son bon fonctionnement
#---------------------------------------------------------#

from machine import Pin,PWM
import time
import sys

sys.path.append('../legs')
from hankle import rotation_hankle_half_pos_turn

# Permet de faire fonctionner le programme de toutes les fonctions importé en continue car la condition ne change jamais
while True:
    rotation_hankle_half_pos_turn()