﻿import random
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
easy = 0
medium = 0
hard = 0
anyW = 0
correct = 0
incorrect = 0

oS = platform.system()
if oS == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

again = 'w'
clear()




def startUp_menu():

    bannerTxt = '''***********************************************
Current --> (Pre)2.2.0 │ Last_Major --> 2.1.0 
***********************************************
'''
    print(Fore.YELLOW + bannerTxt)

    welm =  'Welcome to the spelling game!'
    for l in welm:
        sys.stdout.write(Fore.BLUE + Style.NORMAL + l)
        sys.stdout.flush()
        time.sleep(0.0000000000000000001)

    time.sleep(0.2)
    print()
    txt = '''
Don't forget to read the howToPlay and review your settings!'''
    print(Fore.GREEN + txt)


startUp_menu()
time.sleep(0.1)
print('\n')
print(Fore.CYAN + '1) Play')
time.sleep(0.2)
print('2) Go to settings')
time.sleep(0.2)
print('3) View game related information')
time.sleep(0.2)
print('4) Exit game')
time.sleep(0.2)





print(Fore.MAGENTA + '\nEnter the number of what you would like to do:')


while True:
    flush_input()
    if keyboard.is_pressed('1'):
        option = 1
        break
    elif keyboard.is_pressed('2'):
        option = 2
        break
    elif keyboard.is_pressed('3'):
        option = 3
        break
    elif keyboard.is_pressed('4'):
        option = 4
        break


if option == 2:
    call(['python','Settings.py'])
    sys.exit()

elif option == 3:
    clear()
    clear()
    print(Fore.RED + 'Press enter to continue')
    keyboard.wait('enter')
    clear()
    time.sleep(0.1)
    print(Fore.CYAN + '''1) View user info
2) View game changelog
3) View howToPlay
4) View the point formula (Not coming soon)
''')
    print(Fore.BLUE + '\nPress l to return to main menu')
    print(Fore.MAGENTA + '\nEnter the number of what you would like to do:')


    while True:
        flush_input()
        if keyboard.is_pressed('1'):
            option = 1
            break
        elif keyboard.is_pressed('2'):
            option = 2
            break
        elif keyboard.read_key() == '3':
            call(['python','howToPlay.py'])
            sys.exit()
        elif keyboard.is_pressed('l'):
            clear()
            call(['python', 'classicMode.py'])
            sys.exit()
            
    if option == 1:
        call(['python', 'pData.py'])
        exit()

    elif option == 2:
        changelog = open('changelog.md').read()
        clear()
        print(Fore.WHITE + changelog)
        print(Fore.MAGENTA + '\n(Most recent update is at the top)')
        print(Fore.GREEN + '\nPress enter to continue')
        keyboard.wait('enter')
        clear()
        call(['python', 'classicMode.py'])
        exit()

  

elif option == 4:
    clear()
    flush_input()
    print(Fore.GREEN + 'Closing...')
    sys.exit()
elif option == 5:
    clear()
    call(['python', 'classicMode.py'])
    exit()
elif option == 1:
    clear()
    print(Fore.CYAN + '1) Play Classic mode',Fore.RED + '---------------------- # The main gamemode')
    print()
    time.sleep(0.2)
    print(Fore.CYAN + '2) Play and manage your own sets',Fore.RED + '---------- # Played in the style of Classic mode')
    print()
    time.sleep(0.2)
    print(Fore.CYAN + '3) Other gamemodes',Fore.RED + '------------------------ \
# Unofficial; Just for fun')
    time.sleep(0.2)
    print(Fore.BLUE + '\nPress l to return to main menu')

    print(Fore.MAGENTA + '\nEnter the number of what you would like to do:')
    while True:
        flush_input()
        if keyboard.is_pressed('1'):
            option = 1
            break
        elif keyboard.is_pressed('2'):
            option = 2
            break
        elif keyboard.is_pressed('3'):
            option = 3
            break
        elif keyboard.is_pressed('l'):
            clear()
            call(['python', 'classicMode.py'])
            sys.exit()
            
            

    if option == 2:
        call(['python', 'pWords.py'])
        sys.exit()
    elif option == 3:
        call(['python', 'classicMode+.py'])
        sys.exit()
    else:
        ''

while again == 'w':    
    clear()
    print(Fore.GREEN + '1) Easy')
    time.sleep(0.1)
    print(Fore.YELLOW + '2) Medium')
    time.sleep(0.1)
    print(Fore.RED + '3) Hard')
    time.sleep(0.1)
    if anyWordV == '1':
        print(Fore.MAGENTA + '4) anyWord')
        time.sleep(0.1)
        sMax = 4
    else:
        sMax = 3

    print(Fore.GREEN + '\nChoose a difficulty or press \'p\' to practice: ')
    while True:
        flush_input()
        if keyboard.is_pressed('1'):
            difficulty = 1
            inputM = open('inputM.txt').read()
            break
        elif keyboard.is_pressed('2'):
            difficulty = 2
            inputM = open('inputM.txt').read()
            break
        elif keyboard.is_pressed('3'):
            difficulty = 3
            inputM = open('inputM.txt').read()
            break

        elif sMax == 4 and keyboard.is_pressed('4'):
            difficulty = 4
            break
        
        elif keyboard.is_pressed('p'):
            difficulty = 3
            inputM = '3'
            break 


    easyL = '''Doll Chair Toy Mask Red Brother Honey Lunch Mother Table
Jug	Jelly Eight Piece Friend Camel Family Feast Tree Whale Pony Jump Again Flower Tree Nut
Yellow Simple Drawing Follow Birthday Boat Apple Animal Bell Bounce Crown Castle Drum Dust YakZip
Elephant Ear Fish Foam Glass Guest Hut Hand Ice Ink Jacket Jam Kite Kind Long Lamp Master Mat Nest Night
Orange Owl Parrot Pencil Queen Queue Rose Rest Sweet Sleep Train Tin Uncle Unable Van Vest Water Weep'''.split()

    mediumL = '''accommodation conclusion explanation actually conscience February
alcohol conscious fierce although consequence forty analyse analysis continuous fulfil
argument creation furthermore assessment daughter guard atmosphere decide decision happened
audible definite health audience design height autumn development imaginary beautiful diamond improvise
beginning diary industrial believe disappear interesting beneath disappoint interrupt buried embarrass issue
business energy jealous caught engagement knowledge chocolate enquire listening climb environment lonely
column evaluation lovely concentration evidence marriage material potential sincerely'''.split()
 

    clear()
    if difficulty == 1:
        print(Fore.MAGENTA + 'You have chosen \'easy\' dfficulty')
    elif difficulty == 2:
        print(Fore.MAGENTA + 'You have chosen \'medium\' dfficulty')
    elif difficulty == 3:
        print(Fore.MAGENTA + 'You have chosen \'hard\' dfficulty')
    elif difficulty == 4 and anyWordV == '1':
        print(Fore.MAGENTA + 'You have chosen \'anyWord\' dfficulty')
    print()
    time.sleep(0.5)
    flush_input()
    print(Fore.YELLOW + 'Press enter to confirm and play')
    keyboard.wait('enter')
    print('\n')
    print(Fore.BLUE + '3')
    time.sleep(0.4)
    print()
    print('2')
    time.sleep(0.4)
    print()
    print('1')
    time.sleep(0.4)
    print()
    print('Go!')
    time.sleep(0.75)
    print(Fore.CYAN + '')
    clear()
    
    answerList = []

    again = ''
    questionV = ''
    while again == '':
        randomizer = 0
        print(Fore.CYAN + '')
        clear()
        if difficulty == 1:
            easy += 1
            randomizer = random.randint(0, len(easyL) - 1)
            tLength = 0.6 
            questionV= easyL[randomizer].lower()
            gain = 5 + eGain
            if gain == 0:
                gain = 2
            reduction = 50
        elif difficulty == 2:
            medium += 1
            randomizer = random.randint(0, len(mediumL) - 1)
            tLength = 0.4
            questionV = mediumL[randomizer].lower()
            gain = 10 + eGain
            reduction = 50
        elif difficulty == 3:
            hard += 1
            lines = open('hardWords.txt').read().splitlines()
            tLength = 0.2
            questionV = random.choice(lines)
            gain = 15 + eGain
            reduction = 50
        else:
            anyW += 1
            lines = open('anyWord.txt').read().splitlines()
            tLength = 0.4
            questionV = random.choice(lines)
            gain = 10 + eGain
            reduction = 50
        
        question = []
        for letter in questionV:
            question.append(letter)

        tLength = tLength + (len(question) / 4.75)

        randomizer = 0
        print(questionV)
        time.sleep(tLength)
        clear()

        ## for input1
        if inputM == '1':
            start = time.time()
            print(Fore.GREEN + 'You currently have', points, 'points -----'\
,Fore.CYAN + str(int(answeTimeout) + round(int(len(question) / 4.75))) ,Fore.GREEN + 'seconds (1sf) to answer!')
            print(Fore.MAGENTA + '')
            flush_input()
            while True:
                try:
                    print('Spell the word:\n')
                    answer = inputimeout(prompt = '-> ', timeout = answeTimeout + (len(question) / 4.75)).lower()
                    end = time.time()
                    timeTaken = end - start
                    break
                except TimeoutOccurred:
                    answer = 'Oops you timed out! (Review your settings to change the timeout length)!'
                    break

        elif inputM == '2':
             answer = []
             flag = False
             start = time.time()
             for letter in questionV:
                lLetter = []
         ##for input 2
                if flag == False:
                    while True:
                        try:
                            clear()
                            lLetter = []
                            print(Fore.GREEN + 'You currently have', points, 'points -----',Fore.CYAN + str(int(answeTimeout / 2)) \
,Fore.CYAN + 'seconds (1sf) to enter a letter!')
                            print(Fore.MAGENTA + '')
                            print(''.join(answer))
                            print('Spell the word, letter at a time:\n')
                            flush_input()
                            aLetter = inputimeout(prompt = '-> ', timeout = (answeTimeout / 2)).lower()
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
             end = time.time()
             timeTaken = end - start
        
        else:
            start = time.time()
            answer = []
            for letter in questionV:
                print(Fore.GREEN + 'You currently have', points, 'points')

                print(Fore.MAGENTA + '')
                print(''.join(answer))
                print('Spell the word:')
                while True:
                    if keyboard.is_pressed(letter):
                        answer.append(letter)
                        break
                    elif keyboard.is_pressed('enter'):
                        letter = len(question)
                        break
                clear()
            end = time.time()
            timeTaken = end - start


        clear()
        print(questionV)
        print()
    
        if answer == question or answer == questionV:
            print(Fore.GREEN + 'Correct!')
            correct += 1
            points += int(gain + int((answeTimeout / timeTaken) * 100) / 4)
            print()
            print('+',int(gain + int((answeTimeout / timeTaken) * 100) / 4),'points!')
        else:
            clear()
            print(Fore.RED +  'Incorrect')
            incorrect += 1
            points -= reduction
            print()
            print('-',reduction,'points')
            print()
            print(Fore.MAGENTA + 'You put:', Fore.RED +  ''.join(answer))
            print()
            print(Fore.GREEN + 'Correct answer:',''.join(question))
            
        flush_input()
        if inputM == '1' or inputM == '2':
            print(Fore.BLUE + '''\n\nPress space to play again,
or press '1' to change difficulty,
or press '2' to receive stats and end: ''')

            
            while True:
                flush_input()
                if keyboard.is_pressed(' '):
                    again = ''
                    break
                elif keyboard.is_pressed('1'):
                    again = 'w'
                    break
                elif keyboard.is_pressed('2'):
                    again = 'end'
                    break
            clear()
    
        else:
            print(Fore.BLUE + '''\n\nPress space to play again,
or press '1' to leave practice mode: ''')

            while True:
                if keyboard.is_pressed(' '):
                    again = ''
                    break
                elif keyboard.is_pressed('1'):
                    clear()
                    call(['python', 'classicMode.py'])
                    sys.exit()
        
        if again == 'end':
            break



if inputM == '3':
    call(['python', 'classicMode.py'])
    exit()

print(Fore.GREEN + 'You ended up with', points,'points by the end of this session!')
print('Stats for this session:')
print(Fore.YELLOW + '')

#prints current stats
cStats = open('cStats.txt', 'w')
total = correct + incorrect
total = str(total)
perc = int((correct / int(total)) * 100)
if inputM == '1':
    cInput = 'Input method used: Natural'
elif inputM == '2':
    cInput = 'Input method used: Memorise'
    
elif inputM == '3':
    clear()
    call(['python', 'classicMode.py'])
    sys.exit()

rLines = ['Total points accumulated: '+ str(points),'Total number of questions answered: ' + total, '', cInput, '', str(perc)\
+ '% accuracy',  '', 'Number of quesions answered for each difficulty:','',  'Easy: ' + str(easy),'Medium: '\
+ str(medium),'Hard: ' + str(hard),'AnyWord: ' + str(anyW)]
for line in rLines:
    cStats.write(line)
    cStats.write('\n')
    5
cStats.close()
cStats = open('cStats.txt', 'r')
print(cStats.read())
cStats.close()

#prev stats

pStats = open('pStats.txt', 'r')
time.sleep(0.2)
print('----------------------------------------------------')
time.sleep(0.2)
print(Fore.GREEN + '\nPrevious session stats: ')
time.sleep(0.2)
print(Fore.CYAN + '')
print(pStats.read())
pStats.close()
pStats = open('pStats.txt', 'w')
cStats = open('cStats.txt', 'r')
pStats.write(cStats.read())
cStats.close()
pStats.close()

flush_input()
time.sleep(0.2)
print(Fore.GREEN + 'Press enter to continue:')
keyboard.wait('enter')

clear()
time.sleep(0.2)
bStats = open('bStats.txt', 'r')
print(Fore.GREEN + 'best ever stats in one session: ')
print(Fore.MAGENTA + '')
print(bStats.read())
bStats.close()

bTotal = open('bTotal.txt', 'r')
bTotal = bTotal.readlines()[0]
if int(bTotal) <= points:
    bTotal = open('bTotal.txt', 'w')
    bStats = open('bStats.txt', 'w')
    cStats = open('cStats.txt', 'r')
    bTotal.write(str(points))
    bStats.write(cStats.read())
    bStats.close()
    cStats.close()
    bTotal.close()
    print(Fore.GREEN + '\nWell done new best stats have been recorded and will now be displayed instead of the above from now on!')
else:
    print(Fore.GREEN + 'Best stats are unchanged')

flush_input()
print(Fore.GREEN + 'Press enter to continue:')
keyboard.wait('enter')
clear()
call(['python', 'classicMode.py'])
sys.exit()








  



    



