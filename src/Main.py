import time
import random
import math
import os
import sys



from src.Minigames.Black_Jack_Script import black_Jack
from src.Minigames.Slot_Machine_Script import slot_Machine
from src.Minigames.Roulette_Script import roulette
from src.Minigames.Flip_A_Coin_Script import flip_A_Coin




slot_Machine_Win = False
black_Jack_Win = False
coin_Side = 0


os.system('cls' if os.name == 'nt' else 'clear')

print("=== Casino Blitz ===")
print("You have to get $10k to win")
time.sleep(0.5)
print("Ok lets start")
print("You start with $500 than gample, win = double, loose = loose the bet")






money = 500

while True:
    game_Choice = input("Which game, help for list >").lower()
    
    if game_Choice == "help":
        print("list of games:")
        print("- black jack")
        print("- slot machine")
        print("- roulette")
        print("- coin flip")
        print("Commands:")
        print("- clear")
        print("- exit")
    
    #Black Jack ===========================================
    elif game_Choice == "black jack":
            print("Black jack, please place a bet")
            bet = int(input("$"))
            if bet <= money:
                print(f"bet placed as ${bet}")
                black_Jack()
                if black_Jack_Win == True:
                    bet = bet * 2
                    print(f"You got ${bet}")
                    money = bet + money
                    print(f"You now have ${money}")
                    print("============================")
                elif black_Jack_Win == False:
                    print(f"You lost ${bet}")
                    money = money - bet
                    print(f"You know have ${money}")
                    if money == 0:
                        print("You went broke...")
                        break
            elif bet > money:
                print("Bro bet something you can aford")
    
    #Slot Machine ===========================================
    elif game_Choice == "slot machine":
            print("slot machine, please place a bet")
            bet = int(input("$"))
            if bet <= money:
                print(f"bet placed as ${bet}")
                slot_Machine()
                if slot_Machine_Win == True:
                    bet = bet * 2
                    print(f"You got ${bet}")
                    money = bet + money
                    print(f"You now have ${money}")
                    print("============================")
                elif slot_Machine_Win == False:
                    print(f"You lost ${bet}")
                    money = money - bet
                    print(f"You know have ${money}")
                    print("============================")
                    if money == 0:
                        print("You went broke...")
                        break
                else:
                    print("ERROR")
            elif bet > money:
                print("Bro bet something you can aford")
    #Roulette ======================================================================================
    elif game_Choice == "roulette":
        print("Roulette, please place a bet")
        bet = int(input("$"))
        if bet <= money:
            print(f"bet placed as ${bet}")
            roulette_Win = roulette()
            if roulette_Win == True:
                bet = bet * 2
                print(f"You got ${bet}")
                money = bet + money
                print(f"You now have ${money}")
                print("============================")
            elif roulette_Win == False:
                print(f"You lost ${bet}")
                money = money - bet
                print(f"You know have ${money}")
                print("============================")
                if money == 0:
                    print("You went broke...")
                    break
            else:
                print("ERROR")
        elif bet > money:
            print("Bro bet something you can aford")
    #flip a cpoin ================================================================================
    elif game_Choice == "flip a coin" or game_Choice == "flip coin" or game_Choice == "coin" or game_Choice == "coin flip":
        print("Flip a coin, please place a bet")
        bet = int(input("$"))
        if bet <= money:
            print(f"bet placed as ${bet}")
            coin_Win = flip_A_Coin()
            if coin_Win == True:
                bet = bet * 2
                print(f"You got ${bet}")
                money = bet + money
                print(f"You now have ${money}")
                print("============================")
            elif coin_Win == False:
                print(f"You lost ${bet}")
                money = money - bet
                print(f"You know have ${money}")
                print("============================")
                if money == 0:
                    print("You went broke...")
                    break
            else:
                print("ERROR")
        elif bet > money:
            print("Bro bet something you can aford")

    #Other commands:
    elif game_Choice == "clear":
        # 'cls' for windows, 'clear' for mac/linux (Codespaces is linux)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif game_Choice == "exit":
        sys.exit()
        