#Imports
import sys
import sysconfig
import time
import datetime
from datetime import datetime
import random
import os
from os import system
import json
import tkinter

#Connections
with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json") as f:
    data = json.load(f)

#Role-Verification
def pr_permissions(permi):
    if permi == "permissions.janine.ki.neutral":
        if "permissions.janine.ki.neutral" in data['Permissions']:
            return True
    elif permi == "permissions.janine.ki.manager":
        if "permissions.janine.ki.manager" in data['Permissions']:
            return True
    elif permi == "permissions,janine.ki.administrator":
        if "permissions.janine.ki.administrator" in data['Permissions']:
            return True

#Text-Input
def text():
    Question = input(">>> ")
    if Question in data['Questions'] or Question in data['Questions-Manager'] or Question in data['Questions-Administator']:
        if Question in data['Questions']:
            Response = pr_permissions("permissions.janine.ki.neutral")
            if Response == True:
                index = data['Questions'].index(Question)
                Awnser = data['Response'][index]
                print(Awnser)
                text()
            else:
                print("Dazu hast du keine Berechtigungen!")
                text()
        elif Question in data['Questions-Manager']:
            Response = pr_permissions("permissions.janine.ki.manager")
            if Response == True:
                pass
            else:
                print("Dazu hast du keine Berechtigungen!")
                text()
        elif Question in data['Questions-Administator']:
            pass
    else:
        print("")
        text()

text()