def Multiply():
    Num = 1
    Numbers_To_Multiply = int(input("How Many Numbers You Want to Multiply ---> "))
    for i in range(Numbers_To_Multiply):
        Number = float(input(f"Enter Your {i + 1} Number ---> "))
        Num *= Number
    print(f"Your Multiplication Is ---> {Num}")
