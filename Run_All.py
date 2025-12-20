import subprocess
import sys

Files = [
    ["Advanvce Calculator" , "Advance_Calculator/Calculator.py"],
    ["Attendance Calculator" , "Attendance_Calculator/Calculator.py"],
    ["CGPA Calculator" , "CGPA_Calculator/Calculator.py"],
    ["ChatBot" , "ChatBot/ChatBot.py"],
    ["Excel Search { Under Development }" , "Due To Some Reason It Is In Devlopment..."],
    ["Mouse Tracker" , "Mouse_Tracker/Tracker.py"],
    ["Spammer" , "Spammer/Spammer.py"],
    ["Worm" , "Worm/Worm.py"],
    ["YT PlayList" , "YT_Playlist_Info/Main.py"],
]

while True:

    for i in range(len(Files)):
        if i == 0:
            print("Type The Number For That You Want To Run The File \n")

        print(f"[{i}] ---> {Files[i][0]}")

        if i == len(Files):
            print("[999] ---> Exit")

    File_To_Run = int(input("What You Want To Run ---> "))

    if File_To_Run == 0:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 1:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 2:
        subprocess.run([sys.executable, ])
    elif File_To_Run == 3:
        print("Due To Some Reason It Is In Devlopment...")
    elif File_To_Run == 4:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 5:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 6:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 7:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 8:
        subprocess.run([sys.executable, Files[File_To_Run][1]])
    elif File_To_Run == 999:
        print("Exiting....")
        break
    else:
        print("Wrong Input.... Try Again...")
