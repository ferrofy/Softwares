import os
from Files import File_Maker

def Order_Of_Number(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def Delete_File():
    Files_To_Delete = input("""
               |----> All | Half_50 | Half_100 |
Select From ---|          |         |
               |----> [0] |   [1]   |   [2]    |
                            
[0] All ---> To Delete All Files
[1] Half_50 ---> To Delete First 50% Files 
[2] Half_100 ---> To Delete Last 50% Files
How Much Files You Want To Delete ---> """).lower()

    total = File_Maker.Files_To_Make
    half = total // 2

    if Files_To_Delete in ("all" , "0" , "100"):
        start = 0
        end = total

    elif Files_To_Delete in ("half_50" , "1" , "h50" , "half50"):
        start = 0
        if Order_Of_Number(total) == "Even":
            end = half
        elif Order_Of_Number(total) == "Odd":
            end = half + 1

    elif Files_To_Delete in ("half_100" , "2" , "h100" , "half100"):
        start = half
        end = total

    else:
        print("Wrong Input Try Again...")
        return

    for i in range(start, end):
        file_path = f"{File_Maker.File_Name}_{i}.{File_Maker.Type_Of_File}"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted File ---> {file_path}")
        else:
            print(f"File Not Found ---> {file_path}")
