def Grade_Point_From_Marks(Marks):
    if Marks >= 80:
        return 10
    elif Marks >= 70:
        return 9
    elif Marks >= 50:
        return 8
    elif Marks >= 40:
        return 7

Total_Sem = int(input("Total Semesters Of Course ---> "))
Current_Sem = int(input("Current Semester ---> "))

Total_Credit_Till_Now = 0
Total_Grade_Point_Till_Now = 0

for Sem in range(1, Current_Sem + 1):

    print(f"\n------ Semester {Sem} ------")
    Total_Subject = int(input("Total Subjects ---> "))

    for Sub in range(1, Total_Subject + 1):

        print(f"\nSubject {Sub}")
        Credit_Of_Subject = float(input("Credits Of Subject ---> "))
        Parts_Count = int(input("How Many Parts In Subject ---> "))

        Final_Marks = 0

        for Part in range(1, Parts_Count + 1):

            Part_Name = input(f"Name Of Part {Part} ---> ")
            Part_Percentage = float(input(f"Percentage Of {Part_Name} ---> "))

            if Part_Name.lower() == "st":
                St_1 = float(input("ST 1 Marks ---> "))
                St_2 = float(input("ST 2 Marks ---> "))
                St_3 = float(input("ST 3 Marks ---> "))
                Best_Two = sorted([St_1, St_2, St_3], reverse=True)[:2]
                Avg_St = sum(Best_Two) / 2
                Final_Marks += (Avg_St * Part_Percentage) / 100
            else:
                Marks = float(input(f"Marks Of {Part_Name} ---> "))
                Final_Marks += (Marks * Part_Percentage) / 100

        Grade_Point = Grade_Point_From_Marks(Final_Marks)

        Total_Credit_Till_Now += Credit_Of_Subject
        Total_Grade_Point_Till_Now += Grade_Point * Credit_Of_Subject

        print(f"Final Marks ---> {Final_Marks}")
        print(f"Grade Point ---> {Grade_Point}")

CGPA = Total_Grade_Point_Till_Now / Total_Credit_Till_Now

print("\n==============================")
print(f"CGPA Till Semester {Current_Sem} ---> {CGPA:.2f}")
print("==============================")
