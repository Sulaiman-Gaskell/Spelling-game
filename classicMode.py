import random
import time

from colorama import Back, Fore, Style, init

init()
import os
import platform
import sys
from subprocess import call

from inputimeout import TimeoutOccurred, inputimeout


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

def banner():
    print(Fore.YELLOW + Style.DIM + '''*****************************************
Current --> 2.1.0 │ Last_Major --> 2.1.0 
*****************************************
''')

def beta():
    print(Fore.RED + '''This is currently under development
therefore some features may not work correctly\n''')


while again == 'w':
    banner()


    def welcomeMsg():
        print(Fore.BLUE + Style.NORMAL + 'Welcome to the spelling game!',Fore.CYAN +  '(Backed up by GitHub)')
        time.sleep(0.1)
        print(Fore.GREEN + '''
Don't forget to read the howToPlay and review your settings!''')

    welcomeMsg()

    time.sleep(0.1)
    print('\n')
    print(Fore.CYAN + '''1) Play
2) Go to settings
3) View game related information
4) Exit game
''')

    while True:
        try:
            flush_input()
            print(Fore.MAGENTA + '\nEnter the number of what you would like to do')
            option = int(input('-> '))
            if option > 4 or option < 1:
                option = int('f')
            break
        except ValueError:
            print(Fore.RED + 'Invalid try again' )

    if option == 2:
        clear()
        time.sleep(0.1)
        call(['python','Settings.py'])
        sys.exit()

    elif option == 3:
        clear()
        print(Fore.CYAN + '''1) View user info
2) View game changelog
3) View howToPlay
''')
        while True:
            try:
                time.sleep(0.1)
                flush_input()
                print(Fore.MAGENTA + 'Enter the number of what you would like to do: ')
                option = int(input('-> '))
                if option > 3 or option < 1:
                    option = int('f')
                break
            except ValueError:
                print(Fore.RED + 'Oops this is not avalable yet' )
                print()
                
        if option == 1:
            call(['python', 'pData.py'])
            exit()

        if option == 2:
            changelog = open('changelog.md').read()
            clear()
            print(Fore.WHITE + changelog)
            print(Fore.MAGENTA + '\n(Most recent update is at the top)')
            go = input(Fore.GREEN + '\n►')
            clear()
            call(['python', 'classicMode.py'])
            exit()

        elif option == 3:
            call(['python','howToPlay.py'])
            sys.exit()   

    elif option == 4:
        clear()
        print(Fore.GREEN + 'Closing...')
        sys.exit()
    elif option == 5:
        clear()
        call(['python', 'classicMode.py'])
        exit()
    elif option == 1:
        clear()
        print(Fore.CYAN + '1) Play classic',Fore.RED + '---------------------- #Competitive; with offical scoring')
        print()
        time.sleep(0.2)
        print(Fore.CYAN + '2) Play and manage your own sets',Fore.RED + '----- #Non-competitive; but includes different difficulties')
        print()
        time.sleep(0.2)
        print(Fore.CYAN + '3) Play levels',Fore.RED + '----------------------- \
#Unofficial; multi-word questions which tests your memory and wps')
        time.sleep(0.2)
        print()

        while True:
            try:
                time.sleep(0.1)
                flush_input()
                print(Fore.MAGENTA + '\nEnter the number of what you would like to do: ')
                option = int(input('-> '))
                if option > 3 or option < 1:
                    option = int('f')
                break
            except ValueError:
                print(Fore.RED + 'Oops this is not avalable yet' )
                print()

        if option == 2:
            call(['python', 'pWords.py'])
            sys.exit()
        elif option == 3:
            call(['python', 'pLevels.py'])
            sys.exit()
        else:
            ''


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

    while True:
        try:
            flush_input()
            print(Fore.GREEN + '\nChoose a difficulty: ')
            difficulty = int(input('-> '))
            if difficulty > sMax or difficulty < 1:
                difficulty = int('f')
            break
        except ValueError:
            print(Fore.RED + 'Invalid  try again')
            print()
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
    go = input(Fore.YELLOW + '►')
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
            reduction = 15
        elif difficulty == 2:
            medium += 1
            randomizer = random.randint(0, len(mediumL) - 1)
            tLength = 0.4
            questionV = mediumL[randomizer].lower()
            gain = 10 + eGain
            reduction = 10
        elif difficulty == 3:
            hard += 1
            lines = open('hardWords.txt').read().splitlines()
            tLength = 0.2
            questionV = random.choice(lines)
            gain = 15 + eGain
            reduction = 5
        else:
            anyW += 1
            lines = open('anyWord.txt').read().splitlines()
            tLength = 0.4
            questionV = random.choice(lines)
            gain = 10 + eGain
            reduction = 10
        
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
            print(Fore.GREEN + 'You currently have', points, 'points')
            print(Fore.MAGENTA + '')
            flush_input()
            while True:
                try:
                    print('Spell the word:')
                    answer = inputimeout(prompt = '\n-> ', timeout = answeTimeout + (len(question) / 4.75)).lower()
                    break
                except TimeoutOccurred:
                    answer = 'Oops you timed out! (Review your settings to change the timeout length)!'
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
                            print(Fore.GREEN + 'You currently have', points, 'points')
                            print(Fore.MAGENTA + '')
                            print(''.join(answer))
                            print('Spell the word, letter at a time:')
                            flush_input()
                            aLetter = inputimeout(prompt = '\n-> ', timeout = answeTimeout).lower()
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
            correct += 1
            points += gain
            print()
            print('+',gain,'points!')
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
            
    
        while True:
            try:
                flush_input()
                time.sleep(0.2)
                print(Fore.BLUE + '''\n\nPress enter to play again,
or type 'w' to change difficulty,
or type 'end' to receive stats: ''')
                again = input('\n-> ')
                if again == '' or again == 'w' or again == 'end':
                    break
                else:
                    again = int('f')
            except:
                print(Fore.RED + 'Invalid')
        clear()
        
        if again == 'end':
            break




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
print('----------------------------------------------------')
print(Fore.GREEN + '\nPrevious session stats: ')
print(Fore.CYAN + '')
print(pStats.read())
pStats.close()
pStats = open('pStats.txt', 'w')
cStats = open('cStats.txt', 'r')
pStats.write(cStats.read())
cStats.close()
pStats.close()

flush_input()
go = input(Fore.GREEN + '►')
clear()
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
go = input('\n► ')
clear()
call(['python', 'classicMode.py'])
sys.exit()








  



    



