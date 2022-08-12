import time
import random
from colorama import Fore,Back,Style,init
init()
import os
import sys
from subprocess import call
from inputimeout import inputimeout, TimeoutOccurred
import platform
import keyboard

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    
oS = platform.system()
if oS == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

while True:
    clear()
    print(Fore.CYAN + '''1) View Classic Mode stats
2) View permanent stats (Not coming soon)

press 'l' to leave
    ''')

    time.sleep(0.1)
    print(Fore.MAGENTA + 'Choose an option:')
    while True:
        if keyboard.is_pressed('l'):
            clear()
            call(['python', 'classicMode.py'])
            sys.exit()
        elif keyboard.is_pressed('1'):
            option = 1
            break


    clear()
    if option == 1:
        bStats = open('bStats.txt').read()
        pStats = open('pStats.txt').read()
        print(Fore.GREEN + 'Last Classic Mode game stats:')
        time.sleep(0.2)
        print(Fore.MAGENTA + '----------------------------------------------------')
        time.sleep(0.2)
        print(pStats)
        time.sleep(0.2)        
        print(Fore.GREEN + '\nBest ever recorded Classic Mode game stats:')
        time.sleep(0.2)
        print(Fore.CYAN + '----------------------------------------------------')
        time.sleep(0.2)
        print(bStats)
        time.sleep(0.2)
        print(Fore.GREEN + 'Press enter to continue:')
        keyboard.wait('enter')
        clear()