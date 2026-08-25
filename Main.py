import time
import random
import math
import os
import sys


from Minigames.Black_Jack_Script import black_Jack
from Minigames.Slot_Machine_Script import slot_Machine
from Minigames.Roulette_Script import roulette
from Minigames.Flip_A_Coin_Script import flip_A_Coin




slot_Machine_Win = False
black_Jack_Win = False
coin_Side = 0

invalidate_Run = False

win_Amount = 10000

first_Turn = True

abilty_Tokens = 0

free_Bet = 0
used_Free_Bet = False

bet_Reward = 2

os.system('cls' if os.name == 'nt' else 'clear')

print("=== Casino Blitz ===")
print(f"You have to get ${win_Amount} to win")
print("*to change, use the change command in the choice terminal*")
time.sleep(0.5)
print("Ok lets start")
print("You start with $500 than gample, win = double, loose = loose the bet")


def check_Win():
    if money >= win_Amount:
        if invalidate_Run == False:
            print("Congratulations, you won!")
            print(f"You got ${money} and the win amount was ${win_Amount}")
            credits = input("Do you wish to print credits? (y/n) >").lower()
            if credits == "y" or credits == "yes":
                print("Credits:")
                print("Game Developer: Slushcraft (aka Toast-02)")
                print("Special Thanks: Makaio, Humyle and everyone else who helped test and give feedback")
                print("Also thanks to them for being my friends through my journey of learning how to code and making this game")
                print("And thank YOU for playing!")
            else:
                print("Thanks for playing!")
            sys.exit()
        elif invalidate_Run == True:
            print("Congratulations, you won!")
            print(f"You got ${money} and the win amount was ${win_Amount}")
            print("However, you used a command that invalidates your run, so you can't get the good ending :(")
            credits = input("Do you wish to print credits? (y/n) >").lower()
            if credits == "y" or credits == "yes":
                print("Credits:")
                print("Game Developer: Slushcraft (aka Toast-02)")
                print("Special Thanks: Makaio, Humyle and everyone else who helped test and give feedback")
                print("Also thanks to them for being my friends through my journey of learning how to code and making this game")
                print("And thank YOU for playing!")
            else:
                print("Thanks for playing!")
            sys.exit()



money = 500

while True:
    if first_Turn == True:
        game_Choice = input("Which game, help for list >").lower()
        first_Turn = False
    elif first_Turn == False:
        ability_Choice = input("Would you like to use an ability token for a ranom abilty which can help you or make it harder for you for one token? (y/n) >").lower()
        if ability_Choice == "y" or ability_Choice == "yes":
            if abilty_Tokens >= 1:
                abilty_Tokens -= 1
                print(f"You have {abilty_Tokens} ability tokens left")
                random_Ability = random.randint(1, 4)
                if random_Ability == 1:
                    print("You got +500 dollars!")
                    money += 500
                    print(f"You now have ${money}")
                    check_Win()
                elif random_Ability == 2:
                    print("You got -500 dollars!")
                    money -= 500
                    print(f"You now have ${money}")
                    check_Win()
                elif random_Ability == 3:
                    print("You got a free bet!")
                    print("This means that if you win the next game, you will get double the money, but if you lose, you won't lose any money")
                    print("This ability will be used automatically in the next game you play")
                    free_Bet = 1
                elif random_Ability == 4:
                    print("You got Double Reward for the next game! You will now get x3 the money instead of x2")
                    bet_Reward = 3

                else:
                    print("You don't have any ability tokens to use")

    if game_Choice == "help":
        print("================================================")
        print("list of games:")
        print("- black jack")
        print("- slot machine")
        print("- roulette")
        print("- coin flip")
        print("Commands:")
        print("- clear")
        print("- exit")
        print("- change win amount (WARNING: INVLIDATES RUN)")
        print("- money (WARNING: INVLIDATES RUN)")
        print("- win (WARNING: INVLIDATES RUN)")
        print("================================================")
    
    #Black Jack ===========================================
    elif game_Choice == "black jack":
            if free_Bet >= 1:
                print("You have a free bet, this means that if you win the next game, you will get double the money, but if you lose, you won't lose any money")
                print("This ability will be used automatically in this game")
                free_Bet -= 1
                used_Free_Bet = True
                bet = money
            else:
                print("Black jack, please place a bet")
                bet = int(input("$"))
            if bet <= money:
                print(f"bet placed as ${bet}")
                black_Jack_Win = black_Jack()
                if black_Jack_Win == True:
                    if used_Free_Bet == True:
                        print("You used a free bet, so you doubled your money")
                        used_Free_Bet = False
                        money = money + money
                        bet_Reward = 2
                    else:
                        bet = bet * bet_Reward
                        print(f"You got ${bet}")
                        money = bet + money
                    print(f"You now have ${money}")
                    abilty_Tokens += 1
                    print(f"You have {abilty_Tokens} ability tokens")
                    bet_Reward = 2
                    print("============================")
                elif black_Jack_Win == False:
                    if used_Free_Bet == True:
                        print("You used a free bet, so you lost nothing")
                        used_Free_Bet = False
                        bet_Reward = 2
                    else:
                        print(f"You lost ${bet}")
                        money = money - bet
                    print(f"You know have ${money}")
                    bet_Reward = 2
                    if money == 0:
                        print("You went broke...")
                        break
            elif bet > money:
                print("Bro bet something you can aford")
    
    #Slot Machine ===========================================
    elif game_Choice == "slot machine":
            if free_Bet >= 1:
                print("You have a free bet, this means that if you win the next game, you will get double the money, but if you lose, you won't lose any money")
                print("This ability will be used automatically in this game")
                free_Bet -= 1
                used_Free_Bet = True
                bet = money
            else:
                print("slot machine, please place a bet")
                bet = int(input("$"))
            if bet <= money:
                print(f"bet placed as ${bet}")
                slot_Machine_Win = slot_Machine()
                if slot_Machine_Win == True:
                    if used_Free_Bet == True:
                        print("You used a free bet, so you doubled your money")
                        used_Free_Bet = False
                        money = money + money
                        bet_Reward = 2
                    else:
                        bet = bet * bet_Reward
                        print(f"You got ${bet}")
                        money = bet + money
                    print(f"You now have ${money}")
                    abilty_Tokens += 1
                    print(f"You have {abilty_Tokens} ability tokens")
                    bet_Reward = 2
                    print("============================")
                    check_Win()
                elif slot_Machine_Win == False:
                    if used_Free_Bet == True:
                        print("You used a free bet, so you lost nothing")
                        used_Free_Bet = False
                        bet_Reward = 2
                    else:
                        print(f"You lost ${bet}")
                        money = money - bet
                    print(f"You know have ${money}")
                    bet_Reward = 2
                    print("============================")
                    check_Win()
                    if money == 0:
                        print("You went broke...")
                        break
                else:
                    print("ERROR")
            elif bet > money:
                print("Bro bet something you can aford")
    #Roulette ======================================================================================
    elif game_Choice == "roulette":
        if free_Bet >= 1:
            print("You have a free bet, this means that if you win the next game, you will get double the money, but if you lose, you won't lose any money")
            print("This ability will be used automatically in this game")
            free_Bet -= 1
            used_Free_Bet = True
            bet = money
        else:
            print("Roulette, please place a bet")
            bet = int(input("$"))
        if bet <= money:
            print(f"bet placed as ${bet}")
            roulette_Win = roulette()
            if roulette_Win == True:
                if used_Free_Bet == True:
                    print("You used a free bet, so you doubled your money")
                    used_Free_Bet = False
                    money = money + money
                    bet_Reward = 2
                else:
                    bet = bet * bet_Reward
                    print(f"You got ${bet}")
                    money = bet + money
                print(f"You now have ${money}")
                abilty_Tokens += 1
                print(f"You have {abilty_Tokens} ability tokens")
                bet_Reward = 2
                print("============================")
                check_Win()
            elif roulette_Win == False:
                if used_Free_Bet == True:
                    print("You used a free bet, so you lost nothing")
                    used_Free_Bet = False
                    bet_Reward = 2
                else:
                    print(f"You lost ${bet}")
                    money = money - bet
                print(f"You know have ${money}")
                bet_Reward = 2
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
        if free_Bet >= 1:
            print("You have a free bet, this means that if you win the next game, you will get double the money, but if you lose, you won't lose any money")
            print("This ability will be used automatically in this game")
            free_Bet -= 1
            used_Free_Bet = True
            bet = money
        else:
            print("Flip a coin, please place a bet")
            bet = int(input("$"))
        if bet <= money:
            print(f"bet placed as ${bet}")
            coin_Win = flip_A_Coin()
            if coin_Win == True:
                if used_Free_Bet == True:
                    print("You used a free bet, so you doubled your money")
                    used_Free_Bet = False
                    money = money + money
                    bet_Reward = 2
                else:
                    bet = bet * bet_Reward
                    print(f"You got ${bet}")
                    money = bet + money
                print(f"You now have ${money}")
                abilty_Tokens += 1
                print(f"You have {abilty_Tokens} ability tokens")
                bet_Reward = 2
                print("============================")
                check_Win()
            elif coin_Win == False:
                if used_Free_Bet == True:
                    print("You used a free bet, so you lost nothing")
                    used_Free_Bet = False
                    bet_Reward = 2
                else:
                    print(f"You lost ${bet}")
                    money = money - bet
                print(f"You know have ${money}")
                bet_Reward = 2
                print("============================")
                if money == 0:
                    print("You went broke...")
                    break
            else:
                print("ERROR")
        elif bet > money:
            print("Bro bet something you can aford")
            print("================================================")

    #Other commands:
    elif game_Choice == "clear":
        # 'cls' for windows, 'clear' for mac/linux (Codespaces is linux)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif game_Choice == "exit":
        sys.exit()
    elif game_Choice == "change win amount"or game_Choice == "change win" or game_Choice == "change amount" or game_Choice == "change":
        print("WARNING: THIS INVALIDATES YOUR RUN, ARE YOU SURE YOU WANT TO USE THIS COMMAND?")
        confirmation_Change = input("(y/n) >").lower()
        if confirmation_Change == "y" or confirmation_Change == "yes":
            print("What do you want to change the win amount to?")
            new_Amount = int(input("$"))
            win_Amount = new_Amount
            invalidate_Run = True
            print(f"Win amount changed to ${win_Amount}")
            print("================================================")
            check_Win()
        else:
            print("Command cancelled")
            print("================================================")
    elif game_Choice == "money":
        print("WARNING: THIS INVALIDATES YOUR RUN, ARE YOU SURE YOU WANT TO USE THIS COMMAND?")
        confirmation_Money = input("(y/n) >").lower()
        if confirmation_Money == "y" or confirmation_Money == "yes":
            money = int(input("How much money do you want to have? $"))
            invalidate_Run = True
            print("================================================")
            check_Win()
        else:
            print("Command cancelled")
            print("================================================")
    elif game_Choice == "win":
        print("WARNING: THIS INVALIDATES YOUR RUN, ARE YOU SURE YOU WANT TO USE THIS COMMAND?")
        confirmation_Win = input("(y/n) >").lower()
        if confirmation_Win == "y" or confirmation_Win == "yes":
            invalidate_Run = True
            win_Amount = 1
            money = 9223372036854775807
            print("================================================")
            check_Win()
        else:
            print("Command cancelled")
            print("================================================")

print("The bad ending...")
print("You went broke and lost all your money, better luck next time...")
print("thanks for playing ig, go win the game...")
sys.exit()
        