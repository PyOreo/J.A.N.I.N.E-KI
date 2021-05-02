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

def Enough_Money(amount_out, account):
    Bank = data['Profile']['Bank']
    Wallet = data['Profile']['Wallet']
    if account == "Bank":
        if Bank >= amount_out:
            return True
        else:
            return False
    elif account == "Wallet":
        if Wallet >= amount_out:
            return True
        else:
            return False
    else:
        return False

M = Enough_Money("100", "Bank")
print(M)
