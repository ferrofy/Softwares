def Add():
    Sum = 0
    print("For Addition Just Type Natural Number , For Subtraction Just Use - Sign With It")
    Numbers_To_Add = int(input("How Many Numbers You Have To Add ---> "))
    for i in range(Numbers_To_Add):
        Number = float(input(f"Enter Your {i + 1} Number ---> "))
        Sum += Number
    print(f"Your Addition Is ---> {Sum}")