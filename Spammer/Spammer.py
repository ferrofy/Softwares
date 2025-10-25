# Librarys
import pyautogui
import time
import keyboard
import random

# Basic Info
print("_" * 100)
print("""
      
This Tool Is Made By  |  Team FerroFy  |
To Stop This Tool Press Key --->  'z'

""")

# Basic Needs
print("_" * 100)
Speed = int(input("""

Please Enter Speed From 0 - 10 ---> """))

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
print(f"So User Your Speed is ----> {Speed}")
print(f"So User Time To Spam Is ----> {Time_To_Spam} Sec")
print("_" * 100)

# Variables
Work = True
Message_Sent = 0
Start_Time = time.time()

# All Random Text Which Will Be Sent
All_Texts = [
    "Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry",
    "Blueberry", "Watermelon", "Papaya", "Kiwi", "Lemon", "Lime", "Cherry", "Peach",
    "Plum", "Apricot", "Pomegranate", "Guava", "Coconut", "Fig", "Date", "Raspberry",
    "Blackberry", "Dragonfruit", "Passionfruit", "Jackfruit", "Lychee", "Cantaloupe",
    "Honeydew", "Tangerine", "Mandarin", "Nectarine", "Python", "Java", "C", "C++", "C#",
    "JavaScript", "TypeScript", "Ruby", "Go",
    "Rust", "Kotlin", "Swift", "PHP", "Perl", "Scala", "Dart", "Haskell", "Lua",
    "MATLAB", "R", "Visual Basic", "Objective-C", "Assembly", "Elixir", "F#", "Erlang",
    "Laptop", "Smartphone", "Tablet", "Smartwatch", "Router", "Drone", "VR Headset",
    "Bluetooth Speaker", "USB Drive", "Hard Drive", "SSD", "CPU", "GPU", "RAM",
    "Motherboard", "Power Supply", "Webcam", "Printer", "Keyboard", "Mouse", "Monitor",
    "Microphone", "Headphones", "Charger", "Projector", "Smart TV", "NAS", "IoT Device",
    "Artificial Intelligence", "Machine Learning", "Blockchain", "Cryptocurrency",
    "Cloud Computing", "Docker", "Kubernetes", "Git", "GitHub", "API", "REST", "GraphQL",
    "SQL", "NoSQL", "Firebase", "React", "Angular", "Vue", "Node.js", "Express", "Flask",
    "Django", "Linux", "Windows", "macOS", "Cybersecurity", "Encryption", "VPN", "IoT",
    "5G", "Edge Computing", "Quantum Computing", "Augmented Reality", "Virtual Reality",
    "Rocket", "Satellite", "Mars Rover", "3D Printer", "Electric Car", "Solar Panel",
    "Wind Turbine", "LED Light", "Smart Home", "Robotics", "Nanotechnology",
    "Biotechnology", "Genomics", "Astronomy", "Astrophysics", "Gaming Console",
    "Esports", "Cloud Storage", "Streaming Service", "Smart Glasses",
    "Random" , "Real Human" , "Alfa" , "Beta" , "Gamma" , "Ohm"
]

# Key To Stop Spammer
def on_key(event):
    global Work
    if event.name.lower() == "z":
        Work = False
keyboard.on_press(on_key)

# Speed Redefine
if Speed == 0:
    Speed = Speed
elif Speed < 0 or Speed > 10:
    Work = False
else:
    Speed = Speed / 10

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
        pyautogui.typewrite(random.choice(All_Texts))
        pyautogui.press("enter")
        time.sleep(Speed)
        Message_Sent += 1
else:
    while Work:
        pyautogui.click()
        pyautogui.typewrite(random.choice(All_Texts))
        pyautogui.press("enter")
        time.sleep(Speed)
        Message_Sent += 1
        if Time_To_Spam <= time.time() - Start_Time:
            break

# Exit
print("_" * 100)
print("Total Message_Sent ---> " , Message_Sent)
print("Total Time Used ---> " , time.time() - Start_Time ," Sec")
print("_" * 100)
print("Spammer Stoped")
Exit = input("Press 'Enter' To Exit")