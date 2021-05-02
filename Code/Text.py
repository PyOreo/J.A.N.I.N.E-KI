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

#Add-Custom-Command
def Add_Custom_Command(command, action, argument):
    data['Custom-Commands'].append(command)
    data['Actions'].append(action)
    data['ARG'].append(argument)
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)
    return True

#Remove-Custom-Command
def Remove_Custom_Command(command: str):
    index = data['Custom-Commands'].index(command)
    command = data['Custom-Commands'][index]
    action = data['Actions'][index]
    argument = data['ARG'][index]
    data['Custom-Commands'].remove(command)
    data['Actions'].remove(action)
    data['ARG'].remove(argument)
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)
    return True

#Text-Input
def text():
    Question = input(">>> ")
    if Question in data['Custom-Commands']:
        #Custom-Commands:
        index = data['Custom-Commands'].index(Question)
        action = data['Actions'][index]
        argument = data['ARG'][index]
        if action == "print":
            print(argument)
            print("")
            text()
        #elif action == "<action>"
    elif Question in data['Commands']:
        #Existing-Commands
        if Question == "/help":
            print("/help")
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

def talk():
    print("Oh Hey")
    time.sleep(1)
    print("Wer bist du?")
    QUESTION_1 = input("< [MEIN NAME] > ")
    print(f"Ok. Schön dich kennen zu lernen {QUESTION_1}.")
    time.sleep(3)
    print("Darf ich deinen Namen speichern?")
    QUESTION_2 = input("<JA | NEIN> ")
    if QUESTION_2 == "JA" or QUESTION_2 == "Ja" or QUESTION_2 == "ja":
        data['Profile']['Name'] = QUESTION_2
        data['NEW'] = "False"
        with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
            json.dump(data, f, indent=4)
    elif QUESTION_2 == "NEIN" or QUESTION_2 == "Nein" or QUESTION_2 == "nein":
        print("Ok...")
        data['NEW'] = "True"
        with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
            json.dump(data, f, indent=4)
    time.sleep(3)
    print(f"Darf ich dich was fragen {QUESTION_1}?")
    time.sleep(2)
    QUESTION_3 = input("<Ja, klar | Nein> ")
    if QUESTION_3 == "Ja, klar" or QUESTION_3 == "Ja" or QUESTION_3 == "ja" or QUESTION_3 == "ja, klar":
        time.sleep(3)
        print("Oh, sorry, ich habe gerade eine What'sapp bekommen...")
        time.sleep(2)
        print("Nun zu meiner Frage: Darf ich dich fragen, wie alt du bist?")
        QUESTION_3_1 = input("<JA | NEIN | [DEIN ALTER]>")
        Ja = ['JA', 'Ja', 'ja', 'Auf jeden Fall', 'Klar doch', 'Ok', 'ok']
        Nein = ['NEIN', 'Nein', 'nein', 'Auf keinen Fall', 'Bitte nicht']
        if QUESTION_3_1 in Ja:
            time.sleep(2)
            print("Und wie alt bist du?")
            time.sleep(2)
            QUESTION_3_2 = input("<[DEIN ALTER]> ")
            time.sleep(3)
            print("Ok, ich darf diese Informationen speichern, oder?")
            time.sleep(2)
            QUESTION_3_3 = input("<JA | NEIN> ")
            if QUESTION_3_3 in Ja:
                print("Ok, vielen Dank :)")
                data['Profile']['Age'] = f"{QUESTION_3_2}"
                with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
                    json.dump(data, f, indent=4)
            elif QUESTION_3_3 in Nein:
                time.sleep(3)
                print("Ok, schade...")
        elif QUESTION_3_1 in Nein:
            time.sleep(2)
            print("Ok, schade...")
        else:
            time.sleep(3)
            print("Ok, ich darf diese Informationen speichern, oder?")
            time.sleep(2)
            QUESTION_3_3 = input("<JA | NEIN> ")
            if QUESTION_3_3 in Ja:
                print("Ok, vielen Dank :)")
                data['Profile']['Age'] = f"{QUESTION_3_2}"
                with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
                    json.dump(data, f, indent=4)
            elif QUESTION_3_3 in Nein:
                time.sleep(3)
                print("Ok, schade...")
    time.sleep(3)
    print("Worüber wollen wir uns unterhalten?")
    time.sleep(3)
    QUESTION_4 = input("<[THEMA]> ")
    time.sleep(2)
    if QUESTION_4 == "Python" or QUESTION_4 == "Programmieren":
        print("Da kann ich helfen, aber erzähl mir du doch etwas, ok?")
    else:
        print("Okay, darüber weiß ich zwar nicht so viel, aber du kannst mir ja etwas darüber erzählen, nicht war?")
    time.sleep(2)
    print("Oh... ich habe die Zeit vergessen, ich muss noch los, aber viel Spaß dir noch ;)")
    time.sleep(5)
    text()