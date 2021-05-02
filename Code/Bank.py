import sys
import sysconfig
import datetime
import json
import time
import os
from os import system
import tkinter
import Text

Lang = "DE"

#Connection
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
global ERROR_NOT_ENOUGHT_MONEY
global ERROR_NOT_ENOUGHT_MONEY_IN_WALLET
ERROR_NO_PERMISSIONS = "-"
ERROR_NO_RESULT = "-"
ERROR_NOT_ENOUGH_MONEY = "-"
ERROR_NOT_ENOUGH_MONEY_IN_WALLET = "-"
if Lang == "DE":
    ERROR_NO_PERMISSIONS = data['ERROR-NO_PERMISSIONS_DE']
    ERROR_NO_RESULT = data['ERROR-NO_RESULT_DE']
    ERROR_NOT_ENOUGH_MONEY = data['ERROR_NOT_ENOUGH_MONEY_DE']
    ERROR_NOT_ENOUGH_MONEY_IN_WALLET = data['ERROR_NOT_ENOUGH_MONEY_IN_WALLET_DE']
elif Lang == "EN":
    ERROR_NO_PERMISSIONS = data['ERROR-NO_PERMISSIONS_EN']
    ERROR_NO_RESULT = data['ERROR-NO_RESULT_EN']
    ERROR_NOT_ENOUGH_MONEY = data['ERROR_NOT_ENOUGH_MONEY_EN']
    ERROR_NOT_ENOUGH_MONEY_IN_WALLET = data['ERROR_NOT_ENOUGH_MONEY_IN_WALLET_EN']

#Money-Verification
def Enough_Money(amount: int, account: str):
    Bank = data['Profile']['Bank']
    Wallet = data['Profile']['Wallet']
    if account == "Bank":
        if Bank >= amount:
            return True
        else:
            return False
    elif account == "Wallet":
        if Wallet >= amount:
            return True
        else:
            return False
    else:
        return False

#Add_Money
def Add_Money(amount_in: int, account: str):
    data['Profile'][account] += amount_in
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)

#Remove-Money
def Remove_Money(amount_out: int, account: str):
    M = Enough_Money(amount_out, account)
    if M == True:
        data['Profile'][account] -= amount_out
        with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
            json.dump(data, f, indent=4)

#Set-Money
def Set_Money(amount: int, account: str):
    data['Profile'][account] = amount
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)

#Reset-Account
def Reset_Account(account: str):
    data['Profile'][account] = 0
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)


