import random
import time

def black_Jack():
    card_One = random.randint(1, 10)
    card_Two = 0
    debug_Mode = 0
    cpu_Score = random.randint(17,20)
    global black_Jack_Win

    print("=== Black Jack sim v0.8 ===")
    print("Welcome!")



    while True:
        Choice1 = input("Start game? (y/n) >").lower()
        if Choice1 == "y" or Choice1 == "yes":
            if debug_Mode == 0:
                print("=====================================")
                print("Starting...")
                time.sleep(1.7)
                print("Loading complete!")
                print("=====================================")
                break
            elif debug_Mode == 1:
                print("=====================================")
                print("Starting...")
                time.sleep(0.3)
                print("Imported time")
                time.sleep(0.1)
                print("Imported random")
                time.sleep( 0.1)
                print("Imported math")
                time.sleep(0.1)
                print("Imported sys")
                time.sleep(0.5)
                print("Loading script...[main.py]")
                time.sleep(0.5)
                print("Loading complete!")
                print("=====================================")
                break

        elif Choice1 == "n" or Choice1 == "no":
            print("Exiting...")
            time.sleep(0.3)
            
        
        elif Choice1 == "debug":
            print("Debug mode activated!")
            debug_Mode = 1
        else:
            print("invalid input")
        



    time.sleep(0.5)

    #disply the first card
    print("You pulled",card_One)
    time.sleep(0.5)

    #hit or stand?

    print(f"You have to beat {cpu_Score}")
    
    #this is the actule gp loop
    while True:
        choice = input("Hit or stand? >").lower()
        if choice == "Hit" or choice == "hit":
            print("===========================")
            print("Hitting...")
            time.sleep(0.5)
            card_Two = random.randint(1,10)
            print("you got a",card_Two)
            print("Total cards:",card_Two + card_One)
    
            if card_Two + card_One > 21:
                print("===========================")
                print("You bust!")
                print("Score: INVALID WIN")
                return False
                break
            else:
                card_One = card_Two + card_One
            
        elif choice == "Stand" or choice == "stand":
            print("Standing...")
            time.sleep(0.5)
            print("===========================")
            if cpu_Score <= card_One:
                black_Jack_Win = True
                print("Bang! you got",card_One)
                print("Score:",card_One - 21)
                return True
                break
            elif cpu_Score > card_One:
                print("You lost!")
                black_Jack_Win = False
                return False
                break
        else:
            print("INVALID INPUT")
