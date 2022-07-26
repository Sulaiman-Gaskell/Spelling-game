import time
import random
from colorama import Fore,Back,Style,init
init()
import os
import sys
from subprocess import call
from inputimeout import inputimeout, TimeoutOccurred

def flush_input():
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()
    
clear = lambda: os.system('cls')

inputM = open('inputM.txt', 'r')
inputM = inputM.read()

wAC = open('Wild_animalsC.txt').read()


clear()
print(Fore.RED + 'Please note that all settings (excluding input method) do not affect gameplay here')
go = input(Fore.GREEN + '\nPress enter to continue: ')
clear()

while True:
    print(Fore.GREEN + 'Easy levels:'    1) Wild animals
    2) Electronics''')
    time.sleep(0.1)
    print(Fore.YELLOW + '''
    Medium levels:
    3) Oceanic creatures
    4) Natural disasters''')
    time.sleep(0.1)
    print(Fore.RED + '''
    Hard levels:
    5) Geology
    6) The Atmosphere''')
    time.sleep(0.1)

    while True:
        try:
            wLevel = int(input(Fore.MAGENTA + 'Choose a level to play: '))
            if wLevel > 2 or wLevel < 1:
                wLevel = int('f')
            break
        except:
            print()
            print(Fore.RED + 'This is currently unavaliable')

    if wLevel == 1:
        words = '''Monkey Panda Shark Zebra Gorilla Walrus Leopard Wolf Antelope eagle
Jellyfish Crab Giraffe Woodpecker Camel Starfish Koala Alligator Owl Tiger Bear whale'''.split()
        tLength = 0.8
    elif wLevel == 2:
        words = '''clock charger Bread-maker counter Blender speaker Bulb  Car-toy
fan dryer Computer Copier camera Dishwasher Drill Earphones Fan Fax lamp Headset iPod Juicer Monitor'''.split()
        tLength = 0.8
    ###


