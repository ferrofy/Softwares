import pyautogui
import time
import keyboard
import random

Speed = int(input("Please Enter Speed From 0 - 10 ---> "))
print(f"So User Your Speed is ----> {Speed}")
Message_Sent = 0

All_Texts = [
    # Fruits
    "Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry",
    "Blueberry", "Watermelon", "Papaya", "Kiwi", "Lemon", "Lime", "Cherry", "Peach",
    "Plum", "Apricot", "Pomegranate", "Guava", "Coconut", "Fig", "Date", "Raspberry",
    "Blackberry", "Dragonfruit", "Passionfruit", "Jackfruit", "Lychee", "Cantaloupe",
    "Honeydew", "Tangerine", "Mandarin", "Nectarine",

    # Programming Languages
    "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript", "Ruby", "Go",
    "Rust", "Kotlin", "Swift", "PHP", "Perl", "Scala", "Dart", "Haskell", "Lua",
    "MATLAB", "R", "Visual Basic", "Objective-C", "Assembly", "Elixir", "F#", "Erlang",

    # Tech / Gadgets
    "Laptop", "Smartphone", "Tablet", "Smartwatch", "Router", "Drone", "VR Headset",
    "Bluetooth Speaker", "USB Drive", "Hard Drive", "SSD", "CPU", "GPU", "RAM",
    "Motherboard", "Power Supply", "Webcam", "Printer", "Keyboard", "Mouse", "Monitor",
    "Microphone", "Headphones", "Charger", "Projector", "Smart TV", "NAS", "IoT Device",

    # Tech Concepts / Tools
    "Artificial Intelligence", "Machine Learning", "Blockchain", "Cryptocurrency",
    "Cloud Computing", "Docker", "Kubernetes", "Git", "GitHub", "API", "REST", "GraphQL",
    "SQL", "NoSQL", "Firebase", "React", "Angular", "Vue", "Node.js", "Express", "Flask",
    "Django", "Linux", "Windows", "macOS", "Cybersecurity", "Encryption", "VPN", "IoT",
    "5G", "Edge Computing", "Quantum Computing", "Augmented Reality", "Virtual Reality",
    
    # Misc / Fun
    "Rocket", "Satellite", "Mars Rover", "3D Printer", "Electric Car", "Solar Panel",
    "Wind Turbine", "LED Light", "Smart Home", "Robotics", "Nanotechnology",
    "Biotechnology", "Genomics", "Astronomy", "Astrophysics", "Gaming Console",
    "Esports", "Cloud Storage", "Streaming Service", "Smart Glasses",

    #Others Random Things
    "Random" , "Real Human" , "Alfa" , "Beta" , "Gamma" , "Ohm"
]

Work = True

def on_key(event):
    global Work
    if event.name.lower() == "z":
        Work = False

keyboard.on_press(on_key)

if Speed == 0:
    Speed = Speed
elif Speed < 0 or Speed > 10:
    Work = False
else:
    Speed = Speed / 10

if Work == True:
    print("Starting in 5 seconds...")
    time.sleep(1)
    print("Starting in 4 seconds...")
    time.sleep(1)
    print("Starting in 3 seconds...")
    time.sleep(1)
    print("Starting in 2 seconds...")
    time.sleep(1)
    print("Starting in 1 seconds...")
    time.sleep(1)
else:
    print("Unale To Run. Due To Internal Problem | Possible Error - Speed is More than 10 Or Less Then 0")


while Work:
    pyautogui.click()
    pyautogui.typewrite(random.choice(All_Texts))
    pyautogui.press("enter")
    time.sleep(Speed)
    Message_Sent += 1

print("Total Message_Sent ---> " , Message_Sent)
print("Spammer Stoped")