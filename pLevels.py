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

inputM = open('inputM.txt', 'r')
inputM = inputM.read()

wordsC = open('completion.txt').read().splitlines()



clear()
print(Fore.RED + 'Please note that all settings (excluding input method) do not affect gameplay here\n\n')


while True:
    print(Fore.GREEN + '''Easy levels:
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬''')
    print('1) Wild animals' , Fore.GREEN + ' -completed!' if wordsC[0] == '1' else Fore.RED + ' -incomplete') 
    print(Fore.GREEN + '2) Electronics' , Fore.GREEN + '  -completed!' if wordsC[1] == '1' else Fore.RED + '  -incomplete')
    time.sleep(0.1)
    print(Fore.YELLOW + '''\n
Medium levels:
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬''')
    print('3) Oceanic creatures' , Fore.GREEN + ' -complete!' if wordsC[2] == '1' else Fore.RED + ' -incomplete')
    print(Fore.YELLOW + '4) Natural disasters' , Fore.GREEN + ' -completed!' if wordsC[3] == '1' else Fore.RED + ' -incomplete')
    time.sleep(0.1)
    print(Fore.RED + '''\n
Hard levels:
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬''')
    print('5) Geology' , Fore.GREEN + '        -completed!' if wordsC[4] == '1' else Fore.RED + '        -incomplete')
    print(Fore.RED + '6) The Atmosphere' , Fore.GREEN + ' -completed!' if wordsC[5] == '1' else Fore.RED + ' -incomplete')

    time.sleep(0.1)

    print(Fore.BLUE + '''
Enter 'l' to leave''')
    while True:
        try:
            wLevel = input(Fore.MAGENTA + '\n\nChoose a level to play: ')
            if wLevel == 'l':
                call(['python', 'Spelling_Game.py'])
                exit()
            wLevel = int(wLevel)
            if wLevel > 2 or wLevel < 1:
                wLevel = int('f')
            break
        except ValueError:
            print()
            print(Fore.RED + 'This level is under development and is coming soon')

    clear()
    print(Fore.YELLOW + 'Starting', end='')
    time.sleep(0.9)
    print(' now!')
    time.sleep(0.3)
    clear()
    word = 0
    if wLevel == 1:
        words = '''monkey Panda Shark Zebra Gorilla Walrus Leopard Wolf eagle
Jellyfish Crab Giraffe Camel Starfish Koala Alligator Owl Tiger Bear whale'''.split()
        bTLength = 0.8
        answerTimeout = 5
        indexR = 0
        tWords = '20'

    elif wLevel == 2:
        words = '''clock charger counter Blender speaker Bulb fan dryer Computer
Copier camera Drill Earphones Fan Fax lamp Headset iPod Juicer Monitor'''.split()
        bTLength = 0.8
        answerTimeout = 5
        indexR = 1
        tWords = '20'

    ###

    while word < len(words):
        questionV= words[word].lower()

        question = []
        for letter in questionV:
            question.append(letter)

        tLength = bTLength + (len(question) / 4.75)

        randomizer = 0
        word += 1
        print(Fore.BLUE + str(word) + '/' + tWords)
        word -= 1
        time.sleep(1)
        print('\n')
        print(Fore.GREEN + questionV)
        time.sleep(tLength)
        clear()

                ## for input1
        if inputM == '1':
            print(Fore.MAGENTA + '')
            clear()
            flush_input()
            while True:
                try:
                    answer = inputimeout(prompt = 'Spell the word: ', timeout = answerTimeout + (len(question) / 4.75)).lower()
                    break
                except TimeoutOccurred:
                    answer = 'Oops you timed out! Mayve try an easier level first.'
                    break

        else:
            answer = []
            flag = False
            for letter in questionV:
                lLetter = []
            ##for input 2
                if flag == False:
                    while True:
                        try:
                            clear()
                            lLetter = []
                            print(Fore.MAGENTA + '')
                            clear()
                            print(''.join(answer))
                            flush_input()
                            aLetter = inputimeout(prompt = 'Spell the word, letter at a time: ', timeout = answerTimeout).lower()
                            for l in aLetter:
                                lLetter.append(l)
                            if len(lLetter) == 1:
                                answer.append(aLetter)
                                break
                            else:
                                aLetter = int('f')

                        except TimeoutOccurred:
                            flag = True
                            answer = 'Oops you timed out! (Review your settings to change the timeout length)!'
                            break

                        except:
                            print(Fore.RED + 'Invalid, try again')
                            time.sleep(0.9)
                    
        clear()
        print(questionV)
        print()

        if answer == question or answer == questionV:
            print(Fore.GREEN + 'Correct!')
            print()
            time.sleep(1)
        else:
            clear()
            print(Fore.RED +  'Incorrect')
            print()
            print(Fore.MAGENTA + 'You put:', Fore.RED +  ''.join(answer))
            print()
            print(Fore.GREEN + 'Correct answer:',''.join(question))
            go = input(Fore.MAGENTA + '\nPress enter to continue: ')
            call(['python', 'pLevels.py'])
            exit()

        clear()
        word += 1
    
    if word == len(words):
        print(Fore.GREEN + 'Congrats, you beat this level!\n')
        time.sleep(1)
        go = input(Fore.MAGENTA + 'Press enter to continue: ')
        
        wordsC[indexR] = '1'
        completion = open('completion.txt','w')
        for level in wordsC:
            completion.write(level)
            completion.write('\n')
        completion.close()

        call(['python', 'pLevels.py'])
        exit()
        