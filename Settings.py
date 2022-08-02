import time
import random
from colorama import Fore,Back,Style,init
init()
import os
import sys
from subprocess import call
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
clear()

def beta():
    print(Fore.RED + '''This is currently underdevelopment
therefore some features may not work correctly''')

leave = 'n'


def showSetting():
    inputM = open('inputM.txt', 'r')
    inputM = inputM.read()

    anyWordV = open('anyWordV.txt', 'r')
    anyWordV = anyWordV.read()

    difficultyO = open('difficultyO.txt', 'r')
    difficultyO = difficultyO.read()
    if difficultyO == '1':
        difficultyO = 'Casual'
    elif difficultyO == '2':
        difficultyO = 'Normal'
    elif difficultyO == '3':
       difficultyO = 'Serious'
    elif difficultyO == '4':
      difficultyO = 'Hardcore'
    else:
        difficultyO = 'Too far!'

    print(Fore.CYAN + '1) Toggle input method:',Fore.YELLOW + ('Natural' if inputM == '1' else 'Memorise') + ' mode is selected')
    print(Fore.CYAN + '2) Toggle anyWord',Fore.YELLOW + ('Enabled' if anyWordV == '1' else 'Disabled' ))
    print(Fore.CYAN + '3) Toggle overall difficulty',Fore.YELLOW + difficultyO, 'difficulty is selected' )
    print(Fore.CYAN + '4) Initialise user data')
    print(Fore.CYAN + '5) Reset settings to default')
    print()
    print(Fore.BLUE + '6) Leave settings')


while True:
    showSetting()

    print(Fore.MAGENTA + '\nWhat would you like to do: ')
    while True:
        flush_input()
        if keyboard.is_pressed('1'):
            setting = 1
            break
        elif keyboard.is_pressed('2'):
            setting = 2
            break
        elif keyboard.is_pressed('3'):
            setting = 3
            break
        elif keyboard.is_pressed('4'):
            setting = 4
            break
        elif keyboard.is_pressed('5'):
            setting = 5
            break
        elif keyboard.is_pressed('6'):
            clear()
            call(['python', 'classicMode.py'])
            sys.exit()

         
          
    clear()
    if setting == 1:
        inputM = open('inputM.txt', 'w')
        print(Fore.CYAN + '''1) Natural: type how you would normally, with one whole word at a time

2) Memorise: input the word letter at a time to make you think more and so learn more

(Note: For option 2 when multiple words need to be entered the space will be auto-completed)''')

        time.sleep(0.5)
        print(Fore.MAGENTA + '\nChoose input method: ')
        while True:
            flush_input()
            if keyboard.is_pressed('1'):
                choice = 1
                break
            elif keyboard.is_pressed('2'):
                choice = 2
                break

        if choice == 1:
            inputM.write('1')
        else:
            inputM.write('2')
        print('''
Setting updated''')
        inputM.close()

    elif setting == 2:
        anyWordV = open('anyWordV.txt', 'w')
        print(Fore.CYAN + '''1) Enable anyWord difficulty

2) Disable anyWord difficulty

Why is this a thing? Well anyWord could potentally contain explicit words''')

        time.sleep(0.5)
        print(Fore.MAGENTA + '\nChoose an option: ')
        while True:
            flush_input()
            if keyboard.is_pressed('1'):
                choice = 1
                break
            elif keyboard.is_pressed('2'):
                choice = 2
                break

        if choice == 1:
            anyWordV.write('1')
        else:
            anyWordV.write('2')
        print('''
Setting updated''')
        anyWordV.close()

    elif setting == 3:
        difficultyO = open('difficultyO.txt', 'w')
        print(Fore.CYAN + '''1) Casual (6 seconds), (-5 or -3(easy only) points**)
2) Normal (5 seconds*), (+0 points**)
3) Serious (4 seconds*), (+5 points**)
4) Hardcore (3.5 seconds*), (+10 points**)
5) Too far! (3 seconds*), (+15 points**)

* = to answer; Also gain extra time based on word length of the question
** = per question

Note: This does not affect levels''')

        time.sleep(0.5)
        print(Fore.MAGENTA + '\nChoose a difficulty: ')
        while True:
            flush_input()
            if keyboard.is_pressed('1'):
                choice = 1
                break
            elif keyboard.is_pressed('2'):
                choice = 2
                break
            elif keyboard.is_pressed('3'):
                choice = 3
                break
            elif keyboard.is_pressed('4'):
                choice = 4
                break
            elif keyboard.is_pressed('5'):
                choice = 5
                break

        if choice == 1:
            difficultyO.write('1')
        elif choice == 2:
            difficultyO.write('2')
        elif choice == 3:
            difficultyO.write('3')
        elif choice == 4:
            difficultyO.write('4')
        else:
            difficultyO.write('5')
        print('''
Setting updated''')
        difficultyO.close()

    elif setting == 4:
        print(Fore.MAGENTA + 'Press y to confirm or n to cancel')
        while True:
            if keyboard.is_pressed('n'):
                ''
                break
            elif keyboard.is_pressed('y'):
                wipe = open('pStats.txt', 'w')
                wipe.close()
                wipe = open('cStats.txt', 'w')
                wipe.close()
                wipe = open('bStats.txt', 'w')
                wipe.close()
                wipe = open('bTotal.txt', 'w')
                wipe.write('-9999999999999999999')
                wipe.close()
                wipe = open('completion.txt', 'w')
                wipe.write('0\n0\n0\n0\n0\n0') ########################
                wipe.close()
                print(Fore.GREEN + 'Successfully wiped all user data!')
                time.sleep(1)
                break


        

    elif setting == 5:
        inputM = open('inputM.txt', 'w')
        inputM.write('1')
        difficultyO = open('difficultyO.txt', 'w')
        difficultyO.write('2')
        anyWordV = open('anyWordV.txt', 'w')
        anyWordV.write('1')
        inputM.close()
        difficultyO.close()
        anyWordV.close()
        print(Fore.MAGENTA + 'All reset!')

    time.sleep(0.75)
    print('\n')
    clear()

