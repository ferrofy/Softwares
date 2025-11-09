def Make_File():
    File_To_Make = int(input("How Much Files You Want to Make --->"))
    for i in range(0,File_To_Make):
        File = open(f"Wormed_File_{i}.txt" , "w")
        File.write(f"Wormed File {i}")
        File.close()
        
Make_File()