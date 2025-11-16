def Make_File():
    Files_To_Make = int(input("How Much Files You Want to Make ---> "))
    File_Name = input("What Sould Be Name Of File You Want ---> ")
    Type_Of_File = input("What Type Of File You Want | Default 'txt' ---> ")
    Data_Inside_File = input("What Data You Want Indide File ---> ")
    #Try To make File Like A User Can Add Multiple Lines

    if Type_Of_File == "":
        Type_Of_File == "txt"
    else:
        Type_Of_File = Type_Of_File

    for i in range(0,Files_To_Make):
        File = open(f"{File_Name}{i}.{Type_Of_File}" , "w")
        File.write(Data_Inside_File)
        File.close()

Make_File()