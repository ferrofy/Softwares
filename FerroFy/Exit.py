def Ask_Close():
    Close = input("Press 'Enter' To Exit...")

def Spammer():
    print("_" * 100)
    print("Spammer Stoped")
    Ask_Close()

def Chat_Bot():
    global Close
    Exit_Confirmation = input("\nWant To Exit Y/N ---> ").lower()
    if Exit_Confirmation in ("y","yes"):
        Close = True
    elif Exit_Confirmation in ("n","no"):
        Close = False
    else:
        print("Wrong Input Please Type y/n")
        Chat_Bot()

def Worm():
    print("Bye User Good Luck")
    Ask_Close()

def Calculator():
    print("Bye...")
    Ask_Close()

def YT():
    print("Thank You")
    Ask_Close()