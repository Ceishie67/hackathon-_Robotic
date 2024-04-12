#---------------------------------------------------------#
# Fichier servant a lancer le programme en appelant les fonctions utiles a son bon fonctionnement
#---------------------------------------------------------#

from machine import Pin,PWM
import time
from actions import *
from ankle import *
from hip import *
from knee import *

tmp = 1
# Permet de faire fonctionner le programme de toutes les fonctions importé en continue car la condition ne change jamais
while tmp > 0:
    forward(1)
    tmp -= 1
    
