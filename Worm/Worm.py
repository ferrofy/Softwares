import os
import sys

from Files import File_Maker
from Files import Delete_Files

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from FerroFy import Exit as E
from FerroFy import Entry

Entry.Main_Logo()

File_Maker.Make_File()

Want_To_Delete_Files = input("Did You Want to Delete Files Y / N ---> ")

if Want_To_Delete_Files.lower() in ("y","yes"):
    Delete_Files.Delete_File()
elif Want_To_Delete_Files.lower() in ("n" , "no"):
    print("Will Not Delete Files")
else:
    print("Wrong Input Try Again")

E.Worm()