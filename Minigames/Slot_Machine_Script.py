import time
import random

def slot_Machine():
    slot_One = random.randint(1, 10)
    slot_Two = random.randint(1, 10)
    slot_Three = random.randint(1, 10)

    slot_Machine_Win = False

    print("SLOT MACHINE SIM v0.3")
    print("=== Welcome user! ===")
    time.sleep(1)
    print("you have a 1/1000 chance of winning! Good luck!")
    time.sleep(0.5)
    print("SPINNING...")

    time.sleep(1)

    # roll slot 1:
    if slot_One == 1:
        print("___")
        print("_1_ Slot 1")
    elif slot_One == 2:
        print("___")
        print("_2_ Slot 1")
    elif slot_One == 3:
        print("___")
        print("_3_ Slot 1")
    elif slot_One == 4:
        print("___")
        print("_4_ Slot 1")
    elif slot_One == 5:
        print("___")
        print("_5_ Slot 1")
    elif slot_One == 6:
        print("___")
        print("_6_ Slot 1")
    elif slot_One == 7:
        print("___")
        print("_7_ Slot 1")
    elif slot_One == 8:
        print("___")
        print("_8_ Slot 1")
    elif slot_One == 9:
        print("___")
        print("_9_ Slot 1")
    elif slot_One == 10:
        print("___")
        print("_10_ Slot 1")

    time.sleep(0.5)
    #roll slot 2:
    if slot_Two == 1:
        print("___")
        print("_1_ Slot 2")
    elif slot_Two == 2:
        print("___")
        print("_2_ Slot 2")
    elif slot_Two == 3:
        print("___")
        print("_3_ Slot 2")
    elif slot_Two == 4:
        print("___")
        print("_4_ Slot 2")
    elif slot_Two == 5:
        print("___")
        print("_5_ Slot 2")
    elif slot_Two == 6:
        print("___")
        print("_6_ Slot 2")
    elif slot_Two == 7:
        print("___ Slot 2")
        print("_7_")
    elif slot_Two == 8:
        print("___")
        print("_8_ Slot 2")
    elif slot_Two == 9:
        print("___ Slot 2")
        print("_9_ Slot 2")
    elif slot_Two == 10:
        print("___ Slot 2")
        print("_10_ Slot 2")
    
    time.sleep(0.5)
    #roll slot 3:
    if slot_Three == 1:
        print("___")
        print("_1_ Slot 3")
    elif slot_Three == 2:
        print("___")
        print("_2_ Slot 3")
    elif slot_Three == 3:
        print("___")
        print("_3_ Slot 3")
    elif slot_Three == 4:
        print("___")
        print("_4_ Slot 3")
    elif slot_Three == 5:
        print("___")
        print("_5_ Slot 3")
    elif slot_Three == 6:
        print("___")
        print("_6_ Slot 3")
    elif slot_Three == 7:
        print("___")
        print("_7_ Slot 3")
    elif slot_Three == 8:
        print("___")
        print("_8_ Slot 3")
    elif slot_Three == 9:
        print("___")
        print("_9_ Slot 3")
    elif slot_Three == 10:
        print("___")
        print("_10_ Slot 3")


    time.sleep(0.5)
    print("Checking if you won, be patient...")
    time.sleep(1)

    #checking if user one...

    if slot_One == slot_Two:
        if slot_Two == slot_Three:
            print("OH MY GOD YOU ACTUALLY WON! score = 3")
            return True
            slot_Machine_Win = True
        
        else:
            print("ok you got close, tuff luck bro score = 2 ")
            return False

            slot_Machine_Win = False
    else:
        print("You lose! score = 1")
        return False
        slot_Machine_Win = False
