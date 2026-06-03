import time
import math
import random

def flip_A_Coin():
    while True:
        bet_Coin = input("Heads or tails >").lower()
        if bet_Coin == "heads":
            break
        elif bet_Coin == "tails":
            break
        else:
            print("invalid input")

    Coin_Result = random.randint(0, 1)

    print("Let's flip a coin!")
    time.sleep(.5)

    if Coin_Result == 1:
        print("Heads won!")
        if bet_Coin == "heads":
            return True
        elif bet_Coin == "tails":
            return False
    else:
        print("Tails won!")
        if bet_Coin == "tails":
            return True
        elif bet_Coin == "heads":
            return False
