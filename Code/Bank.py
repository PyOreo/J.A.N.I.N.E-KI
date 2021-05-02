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
    data['Profile']['Currency-Symbol'] = "\u20ac"
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)
elif data['Profile']['Language'] == "EN":
    Lang = "EN"
    data['Profile']['Currency-Symbol'] = "$"
    with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
        json.dump(data, f, indent=4)

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

#Deposit
def Deposit(amount: int):
    M = Enough_Money(amount, "Wallet")
    if M == True:
        data['Profile']['Wallet'] -= amount
        data['Profile']['Bank'] += amount
        with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
            json.dump(data, f, indent=4)
        return True

#Withdraw
def Withdraw(amount):
    M = Enough_Money(amount, "Bank")
    if M == True:
        data['Profile']['Bank'] -= amount
        data['Profile']['Wallet'] += amount
        with open(fr"C:\Users\{os.getlogin()}\Documents\GitHub\J.A.N.I.N.E-KI\Code\Data.json", "w+") as f:
            json.dump(data, f, indent=4)
        return True

#Balance
def Balance():
    Bank = data['Profile']['Bank']
    Wallet = data['Profile']['Wallet']
    Currency = data['Profile']['Currency-Symbol']
    print(f" Bank: {Bank}{Currency} \n\n Wallet: {Wallet}{Currency}")

Balance()