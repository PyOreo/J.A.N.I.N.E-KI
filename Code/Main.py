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
import Text
import Games

#Display license

def display_license():
    with open(fr'C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\LICENSE.txt', 'r') as file:
        data = file.read()
    print(data)
    print("")
    with open(fr'C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json') as f:
        data = json.load(f)
    if data['NEW'] == "False":
        Text.text()
    elif data['NEW'] == "True":
        Text.talk()
    else:
        Text.talk()
    
display_license()