def Per_Subject_Attendence(Subject_Name="Unknown Subject"):
    global Data , Total_Classes , Total_Classes_Attended , Total_OD , Pending_OD ,Current_Attendance , Upcomming_Attendance
    Total_Classes = int(input("Total Number Of Classes ---> "))
    Total_Classes_Attended = int(input("Total Number Of Classes Attended ---> "))
    Total_OD = int(input("Total Number Of OD Approved ---> "))
    Pending_OD = int(input("Pending OD ---> "))

    Current_Attendance = round(((Total_Classes_Attended + Total_OD) / Total_Classes) * 100, 2)
    Upcomming_Attendance = round(((Total_Classes_Attended + Total_OD + Pending_OD) / Total_Classes) * 100, 2)

    print("_" * 100)

    Data = f"""

_______________________ {Subject_Name} _______________________
Total Attendence ---> {Current_Attendance} %
Total Attendence After All OD ---> {Upcomming_Attendance} %
{Classes_For_65()}
{Classes_For_75()}

"""
    print(Data)
    print("_" * 100)

def Save_File(Name_Of_File, Data):
    File = open(f"{Name_Of_File}.txt", f"w")
    File.write(Data)
    File.close()

def Classes_For_65():
    global Upcomming_Classes_Needed , Classes_Needed , Net_Attendance
    Classes_Needed = 0
    Upcomming_Classes_Needed = 0
    Net_Attendance = Current_Attendance
    Upcomming_Net_Attendance = Upcomming_Attendance

    if Net_Attendance < 65:
        while Net_Attendance < 65:
            Classes_Needed += 1
            if Net_Attendance >= 65:
                break
            else:
                Net_Attendance = round(((Total_Classes_Attended + Total_OD + Classes_Needed) / Total_Classes) * 100, 2)

        while Upcomming_Net_Attendance < 65:
            Upcomming_Classes_Needed += 1
            if Upcomming_Net_Attendance >= 65:
                break
            else:
                Upcomming_Net_Attendance = round(((Total_Classes_Attended + Total_OD + Pending_OD + Upcomming_Classes_Needed) / Total_Classes) * 100, 2)

        return f"Classes Needed For 65% [Without Pending OD] ----> {Upcomming_Classes_Needed} \nClasses Needed For 65% [With Pending OD] ----> {Classes_Needed}"

    else:
        return f"You Alerady Have 65% Attendence In {Subject_Name}"


def Classes_For_75():
    global Upcomming_Classes_Needed , Classes_Needed , Net_Attendance
    Classes_Needed = 0
    Upcomming_Classes_Needed = 0
    Net_Attendance = Current_Attendance
    Upcomming_Net_Attendance = Upcomming_Attendance

    if Net_Attendance < 75:
        while Net_Attendance < 75:
            Classes_Needed += 1
            if Net_Attendance >= 75:
                break
            else:
                Net_Attendance = round(((Total_Classes_Attended + Total_OD + Classes_Needed) / Total_Classes) * 100, 2)
        while Upcomming_Net_Attendance < 75:
            Upcomming_Classes_Needed += 1
            if Upcomming_Net_Attendance >= 75:
                break
            else:
                Upcomming_Net_Attendance = round(((Total_Classes_Attended + Total_OD + Pending_OD + Upcomming_Classes_Needed) / Total_Classes) * 100, 2)
        return f"Classes Needed For 75% [Without Pending OD] ----> {Upcomming_Classes_Needed} \nClasses Needed For 75% [With Pending OD] ----> {Classes_Needed}"

    else:
        return f"You Alerady Have 75% Attendence In {Subject_Name}"

Num_Of_Sub = int(input("Number Of Subjects You Have ----> "))

for i in range(Num_Of_Sub):
    Subject_Name = input(f"Your {i+1} Subject Name ----> ")
    Per_Subject_Attendence(Subject_Name)

    Save_In_File = input("Want to Save This In A File Y/N ----> ")
    if Save_In_File.lower() in ("y", "yes"):
        Name_Of_File = input("What Should Be Name Of File ----> ")
        Save_File(Name_Of_File, Data)
    elif Save_In_File.lower() in ("n", "no"):
        print(f"{Subject_Name} Data Flushed...")
    else:
        print("Wrong Input...")
