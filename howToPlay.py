import time
import random
from colorama import Fore,Back,Style,init
init()
import os
import sys
from subprocess import call
import platform

oS = platform.system()
if oS == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')
clear()
time.sleep(0.1)

print(Fore.GREEN + 'Welcome to The Spelling Game! (► = press enter)')
print(Fore.YELLOW + '''-----------------------------------------------------------------------------------------------------------------------
This is where a word is shown on your screen which then disappears after a few seconds.
You then have to type that word in afterwards when prompted to.
Gain points by answering correctly and compare your scores to previous sesssions''')
go = input(Fore.GREEN + '►')
print(Fore.BLUE + '''----------------------------------------------------------------------------------------------------------------------- 
The time at which the word is shown for is based on your SELECTED DIFFICULTY and the LENGTH OF THE WORD given,
SELECTED DIFFICULTY is chosen when starting a game.''')
go = input(Fore.GREEN + '►')
print(Fore.MAGENTA + '''-----------------------------------------------------------------------------------------------------------------------
For both types of difficulty, the harder the difficulty selected the more points gained per correct question,
so you could do a combo for the maxium points but BEWARE, you will also lose more points.''')
go = input(Fore.GREEN + '►')
print(Fore.LIGHTYELLOW_EX + '''-----------------------------------------------------------------------------------------------------------------------
You only have a certain amount of time to answer each question. Either per word or letter based on your input method.
This time is affected by LENGTH OF WORDS and OVERALL DIFFICULTY which can be changed in settings.''')
go = input(Fore.GREEN + '►')
print(Fore.LIGHTMAGENTA_EX + Style.DIM + '''-----------------------------------------------------------------------------------------------------------------------
SETTINGS: change how the game plays and feels to your likeing. Here you can also clear all user data.
Input method: enter either a word or letter at a time. Entering a word is harder because you will have less effective time to answer,
but it is more NATURAL. Letter at a time allows for you to easily MEMORISE a word.''')

go = input(Fore.GREEN + Style.NORMAL + '►')
print(Fore.CYAN + '''-----------------------------------------------------------------------------------------------------------------------
ANYWORD difficulty is a special selectable difficulty which can be disabled in settings.
It contains over 4000000 words from the English language.''')
go = input(Fore.GREEN + '►')
print(Fore.RED + '''-----------------------------------------------------------------------------------------------------------------------
STATS: at the end of every session, the current, previous and best session's stats will be displayed.
Use this to improve and see your spelling ability.''')
go = input(Fore.GREEN + '►')
print(Fore.LIGHTCYAN_EX + '''-----------------------------------------------------------------------------------------------------------------------
You can create and manage your own set of words. 
Play your own set of words to improve your spelling on a certain set of words!''')
go = input(Fore.GREEN + '►')
print(Fore.LIGHTGREEN_EX + '''-----------------------------------------------------------------------------------------------------------------------
Play levels to try and beat (spell all words correctly) sets of words which vary in difficulty.
Getting even one question wrong results in you having to starts over again!
(User data here can also be wiped in settings alongs with preset stats)''')

print()
go = input(Fore.GREEN + 'Press enter to continue: ')
clear()
call(['python', 'Spelling_Game.py'])
sys.exit()