import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from FerroFy import Exit as Exit_File

Exit_File.Exit = False

while not Exit_File.Exit:
    Exit_File.Chat_Bot()