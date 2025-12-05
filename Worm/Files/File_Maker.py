Files_To_Make = 0
File_Name = ""
Type_Of_File = ""
Data_Inside_File = ""

def Make_File():
    global Files_To_Make, File_Name, Type_Of_File, Data_Inside_File
    Files_To_Make = int(input("How Much Files You Want to Make ---> "))
    File_Name = input("What Should Be Name Of File You Want ---> ")
    Type_Of_File = input("What Type Of File You Want | Default 'txt' ---> ")
    Data_Inside_File = input("What Data You Want Inside File ---> ")

    if Type_Of_File == "":
        Type_Of_File = "txt"

    for i in range(Files_To_Make):
        f = open(f"{File_Name}_{i}.{Type_Of_File}", "w")
        f.write(Data_Inside_File)
        f.close()
