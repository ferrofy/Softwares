import sys
import os

from Files import Addition
from Files import Multiplication
from Files import Division
from Files import Average
from Files import Determinant

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from FerroFy import Exit
from FerroFy import Entry

Entry.Main_Logo()

Action = input("""
        --------|  Basic  |--------
                   
[0] ---> Addition / Subtraction
[1] ---> Multiplication
[2] ---> Division
[3] ---> Average
                   
        --------|  Advanced  |--------
                   
[000] ---> Determinant Of Matrix
[001] --->  { Comming Soon }
[002] ---> 
[003] ---> 
[003] ---> 
[004] --->

What Operation You Want To Preform ----> """).strip()


if Action == "0":
    Addition.Add()
elif Action == "1":
    Multiplication.Multiply()
elif Action == "2":
    Division.Divide()
elif Action == "3":
    Average.Avg()
elif Action == "000":
    Determinant.Det()

    
else:
    print("Wrong Input...")

Exit.Calculator()