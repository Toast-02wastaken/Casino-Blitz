import time
import random
import math
import os
import sys

red_Or_Black = input("Red or black? >").lower()

if red_Or_Black == "red":
    choice = "red"
if red_Or_Black == "black":
    choice = "black"

random_Answer = random.randint(1, 2)

