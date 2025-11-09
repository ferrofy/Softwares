# Librarys
import pyautogui
import time
import keyboard
import random

from Files import Spamming_Text
from Files import Entry
from Files import Speed as Speed

#Logo
Entry.Logo_Entrance()

# Basic Info
Entry.Basic_Info()

# Basic Needs
Speed.Set_Speed()

print("_" * 100)
Time_To_Spam = int(input("""

For Infinity Select '0'
Else Select From 1 - Infinity
For How Much Sec You Wanana Attack ---> """))

# Time To Spam Redefine
if Time_To_Spam == 0:
    Time_To_Spam = "Infinity"
else:
    Time_To_Spam = Time_To_Spam

# Basic Need Review
print("_" * 100)
print(f"So User Your Speed is ----> {Speed.Speed}")
print(f"So User Time To Spam Is ----> {Time_To_Spam} Sec")
print("_" * 100)

# Variables
Work = True
Message_Sent = 0
Start_Time = time.time()

# Key To Stop Spammer
def on_key(event):
    global Work
    if event.name.lower() == "z":
        Work = False
keyboard.on_press(on_key)

# Speed Redefine
if Speed.Speed == 0:
    Speed.Speed = Speed.Speed
elif Speed.Speed < 0 or Speed.Speed > 10:
    Work = False
else:
    Speed.Speed = Speed.Speed / 10

# Timer
if Work == True:
    for i in range(5,0,-1):
        print(f"Running Spammer in {i} Sec")
        time.sleep(1)
else:
    print("Unale To Run. Due To Internal Problem | Possible Error - Speed is More than 10 Or Less Then 0")

#Main Spammer Loop
if Time_To_Spam == "Infinity":
    while Work:
        pyautogui.click()
        pyautogui.typewrite(random.choice(Spamming_Text.Spamming_Texts))
        pyautogui.press("enter")
        time.sleep(Speed.Speed)
        Message_Sent += 1
else:
    while Work:
        pyautogui.click()
        pyautogui.typewrite(random.choice(Spamming_Text.Spamming_Texts))
        pyautogui.press("enter")
        time.sleep(Speed.Speed)
        Message_Sent += 1
        if Time_To_Spam <= time.time() - Start_Time:
            break

# Exit
print("_" * 100)
print("Total Message_Sent ---> " , Message_Sent)
print("Total Time Used [Approx] ---> " , round(time.time() - Start_Time , 2)," Sec")
print("_" * 100)
print("Spammer Stoped")
Exit = input("Press 'Enter' To Exit")