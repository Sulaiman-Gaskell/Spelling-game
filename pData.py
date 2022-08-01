import time
import random
from colorama import Fore,Back,Style,init
init()
import os
import sys
from subprocess import call
from inputimeout import inputimeout, TimeoutOccurred
import platform

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
2) View permanent stats (Coming soon)

press 'l' to leave
    ''')

    while True:
        try:
            time.sleep(0.1)
            print(Fore.MAGENTA + 'Choose an option:')
            option = (input('-> '))
            if option == 'l':
                clear()
                call(['python', 'classicMode.py'])
                sys.exit()

            option = int(option)
            if option > 1 or option < 1:
                option = int('f')
            break
        except:
            print(Fore.RED + 'This is currently not available')
            print()

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
        go = input(Fore.GREEN + '\n►')
        clear()