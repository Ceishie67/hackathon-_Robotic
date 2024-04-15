from machine import Pin,PWM
import time
from ankle import *
from hip import *
from knee import *

while True:
    rotation_Rknee_half_pos_turn(0.1)
    rotation_Rknee_return_neutral_pos(0.1)
    rotation_Rknee_half_neg_turn(0.1)
    rotation_Rknee_return_neutral_neg(0.1)
    rotation_Lknee_half_neg_turn(0.1)
    rotation_Lknee_return_neutral_neg(0.1)
    rotation_Lknee_half_pos_turn(0.1)
    rotation_Lknee_return_neutral_pos(0.1)