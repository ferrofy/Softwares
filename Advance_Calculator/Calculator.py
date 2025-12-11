import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from FerroFy import Exit
from FerroFy import Entry

Entry.Main_Logo()

Action = int(input("""
[0] ---> Addition
[1] ---> Subtraction
[1] ---> Multiply
[2] ---> Division

[3] ---> 
[4] ---> 
[5] ---> 
[6] ---> 
[7] ---> 
[8] ---> 
[9] --->

What Operation You Want To Preform ----> """))


Exit.Calculator()