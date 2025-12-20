def Avg():
    Sum = 0
    Total_Numbers = int(input("How Many Numbers You Have ---> "))
    for i in range(Total_Numbers):
        Number = float(input(f"Enter Your {i + 1} Number ---> "))
        Sum += Number
    Average = Sum / Total_Numbers
    print(f"Your Average Is ---> {Average}")