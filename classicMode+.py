import random
import time

from colorama import Back, Fore, Style, init

init()
import os
import platform
import sys
from subprocess import call

from inputimeout import TimeoutOccurred, inputimeout
import keyboard

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys  # for linux/unix
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

inputM = open('inputM.txt', 'r')
inputM = inputM.read()

anyWordV = open('anyWordV.txt', 'r')
anyWordV = anyWordV.read()

difficultyO = open('difficultyO.txt', 'r')
difficultyO = open('difficultyO.txt', 'r')
difficultyO = difficultyO.read()
if difficultyO == '1':
    answeTimeout = 6
    eGain = -5
elif difficultyO == '2':
    answeTimeout = 5
    eGain = 0
elif difficultyO == '3':
    answeTimeout = 4
    eGain = 5
elif difficultyO == '4':
    answeTimeout = 3.5
    eGain = 10
else:
    answeTimeout = 3
    eGain = 15

points = 0

oS = platform.system()
if oS == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

again = 'w'
clear()

print(Fore.CYAN + '1) Play Classic_mode+', Fore.RED + '--------------------- # Classic mode, with a twist!')###
print()
time.sleep(0.2)
print(Fore.CYAN + '2) Play levels', Fore.RED + '---------------------------- # Word catagories that test wps and memory')
time.sleep(0.2)
print()
print(Fore.BLUE + 'Press l to leave')

print(Fore.MAGENTA + '\nWhat would you like to do: ')
while True:
    if keyboard.is_pressed('2'):
        clear()
        call(['python', 'pLevels.py'])
        sys.exit()
    elif keyboard.is_pressed('l'):
        clear()
        call(['python', 'classicMode.py'])
        sys.exit()