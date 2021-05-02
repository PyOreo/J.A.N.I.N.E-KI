import sys
import sysconfig
import time
import tkinter
import os
import random
from os import system
import Text
import Bank

def slots():
    chance = ['🍋', '🍊', '🍎', '🥇']
    emoji_1 = random.choice(chance)
    emoji_2 = random.choice(chance)
    emoji_3 = random.choice(chance)
    all = f"{emoji_1}{emoji_2}{emoji_3}"
    return all



