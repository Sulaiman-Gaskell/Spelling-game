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

oS = platform.system()
if oS == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

def pBar():
    clear()
    timer = 0.05
    def rep():
        print('\nPress enter to continue:')
        keyboard.wait('enter')
        clear()
    clear()
    def pBar1():
        bar = ['║']
        space = ' - - - - - - - -'.split('-')
        print(end='')
        count = 9
        while count > 0:
            clear()
            bar.append('■')
            print(''.join(bar)+''.join(space) + '║          ║          ║          ║')
            print(Fore.WHITE + '\nLoading.')
            time.sleep(timer)
            count -= 1
            del space[0]
    
    def pBar2():
        bar = ['║']
        space = ' - - - - - - - -'.split('-')
        print(end='')
        count = 9
        while count > 0:
            clear()
            bar.append('■')
            print('║■■■■■■■■■■'+''.join(bar)+''.join(space) + '║          ║          ║')
            print('\nLoading..')
            time.sleep(timer)
            count -= 1
            del space[0]
    
    def pBar3():
        bar = ['║']
        space = ' - - - - - - - -'.split('-')
        print(end='')
        count = 9
        while count > 0:
            clear()
            bar.append('■')
            print('║■■■■■■■■■■║■■■■■■■■■■'+''.join(bar)+''.join(space) + '║          ║')
            print('\nLoading...')
            time.sleep(timer)
            count -= 1
            del space[0]
    
    def pBar4():
        bar = ['║']
        space = ' - - - - - - - -'.split('-')
        print(end='')
        count = 9
        while count > 0:
            clear()
            bar.append('■')
            print('║■■■■■■■■■■║■■■■■■■■■■║■■■■■■■■■■'+''.join(bar)+''.join(space) + '║')
            print('\nLoading....')
            time.sleep(timer)
            count -= 1
            del space[0]

    pBar1()
    time.sleep(0.3)
    pBar2()
    time.sleep(0.3)
    pBar3()
    time.sleep(0.3)
    pBar4()
    time.sleep(0.3)
    

pBar()
call(['python', 'classicMode.py'])