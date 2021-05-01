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

#Language
global Lang
Lang = "DE"

#Connections
with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json") as f:
    data = json.load(f)

#Language for ERROR
if data['Profile']['Language'] == "DE":
    Lang = "DE"
elif data['Profile']['Language'] == "EN":
    Lang = "EN"

#ERROR
global ERROR_NO_PERMISSIONS
global ERROR_NO_RESULT
ERROR_NO_PERMISSIONS = "-"
ERROR_NO_RESULT = "-"
if Lang == "DE":
    ERROR_NO_PERMISSIONS = data['ERROR-NO_PERMISSIONS_DE']
    ERROR_NO_RESULT = data['ERROR-NO_RESULT_DE']
elif Lang == "EN":
    ERROR_NO_PERMISSIONS = data['ERROR-NO_PERMISSIONS_EN']
    ERROR_NO_RESULT = data['ERROR-NO_RESULT_EN']

#Language-Verification
def pr_language(lang):
    if lang == "DE":
        DE = True
        return DE
    elif lang == "EN":
        EN = True
        return EN
    else:
        return False

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
    if Question in data['Commands']:
        index = data['Commands'].index(Question)
        action = data['Actions'][index]
        argument = data['ARG'][index]
        if action == "print":
            print(argument)
            print("")
            text()
    elif Question in data['Questions'] or Question in data['Questions-Manager'] or Question in data['Questions-Administator']:
        if Question in data['Questions']:
            Response = pr_permissions("permissions.janine.ki.neutral")
            if Response == True:
                index = data['Questions'].index(Question)
                Awnser = data['Response'][index]
                print(Awnser)
                print("")
                text()
            else:
                print(ERROR_NO_PERMISSIONS)
                print("")
                text()
        elif Question in data['Questions-Manager']:
            Response = pr_permissions("permissions.janine.ki.manager")
            if Response == True:
                index = data['Questions-Manager'].index(Question)
                Awnser = data['Response-Manager'][index]
                print(Awnser)
                print("")
                text()
            else:
                print(ERROR_NO_PERMISSIONS)
                print("")
                text()
        elif Question in data['Questions-Administator']:
            Response = pr_permissions("permissions,janine.ki.administrator")
            if Response == True:
                index = data['Question-Administrator'].index(Question)
                Awnser = data['Response-Administrator'][index]
                print(Awnser)
                print("")
                text()
            else:
                print(ERROR_NO_PERMISSIONS)
                print("")
                text()
    else:
        print(ERROR_NO_RESULT)
        print("")
        text()

text()