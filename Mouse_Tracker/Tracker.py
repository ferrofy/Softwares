import keyboard
import pyautogui
import time
from datetime import datetime

Work = True
Time_Of_Record = int(input("""Select Speed From 1 - 100 Units  |  10 Units = 1 Sec
What Will Be Frequency For Recording Mouse Moment ---> """))

if 1 <= Time_Of_Record <= 100:
    Time_Of_Record = Time_Of_Record / 10
else:
    print("Wrong Input Of Time , Exiting....")
    Work = False

def on_key(Clicked_key):
    global Work
    if Clicked_key.name.lower() == "z":
        Work = False

keyboard.on_press(on_key)

while Work:
    Mouse_Position = pyautogui.position()
    Time = datetime.now().strftime("%I:%M:%S %p  |  %d/%m/%y")
    print(f"X-Axis ---> {Mouse_Position.x} | Y-Axis ---> {Mouse_Position.y} At Time ----> {Time}")
    File = open("Mouse_Data.txt", "a")
    File.write(f"X-Axis ---> {Mouse_Position.x} | Y-Axis ---> {Mouse_Position.y} At Time ----> {Time}\n")
    File.close()
    time.sleep(Time_Of_Record)

Exit = input("Press Enter To Exit....")