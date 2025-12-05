def Tracker_Exit():
    print("_" * 100)
    print("Spammer Stoped")
    Close = input("Press 'Enter' To Exit...")

def Chat_Bot_Exit():
    global Exit
    Exit_Confirmation = input("\nWant To Exit Y/N ---> ").lower()
    if Exit_Confirmation in ("y","yes"):
        Exit = True
    elif Exit_Confirmation in ("n","no"):
        Exit = False
    else:
        print("Wrong Input Please Type y/n")
        Chat_Bot_Exit()

def Worm_Exit():
    print("Bye User Good Luck")
    Close = input("Press Enter To Exit...")