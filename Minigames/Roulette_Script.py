import time
import random
import math
import os
import sys



def roulette():

    

   

    red_Or_Black = input("Red or black? >").lower()

    if red_Or_Black == "red":
        choice = "red"
    if red_Or_Black == "black":
        choice = "black"

    random_Picker = random.randint(1, 2)
    #1 = red
    #2 = black

    print("Rolling...")
    time.sleep(1)

    if random_Picker == 1:
        print("It's red!")
    elif random_Picker == 2:
        print("It's black!")

    if random_Picker == 1:
        if choice == "red":
            print("You won!")
            return True
        else:
            print("You lost...")
            return False
    elif random_Picker == 2:
        if choice == "black":
            print("You won!")
            return True
        else:
            print("You lost...")
            return False