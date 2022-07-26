import time
from inputimeout import inputimeout, TimeoutOccurred
import random
from colorama import Fore,Back,Style,init
init()
import os
import sys
from subprocess import call

clear = lambda: os.system('cls')
clear()

def flush_input():
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

questionV = '\n'

inputM = open('inputM.txt', 'r')
inputM = inputM.read()

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

gain = 10 + eGain
reduction = 10

points = 0
correct = 0
incorrect = 0
again = ''
total = 0

def beta():
    print(Fore.RED + '''This is currently underdevelopment
therefore some features may not work correctly
''')

wordCheck1 = open('pWords1.txt', 'r')
wordCheck1 = wordCheck1.read().split()

wordCheck2 = open('pWords2.txt', 'r')
wordCheck2 = wordCheck2.read().split()

wordCheck3 = open('pWords3.txt', 'r')
wordCheck3 = wordCheck3.read().split()

wordCheck4 = open('pWords4.txt', 'r')
wordCheck4 = wordCheck4.read().split()

wordCheck5 = open('pWords5.txt', 'r')
wordCheck5 = wordCheck5.read().split()

cSet = ''
while cSet != 'leave':

    set1T = open('pWords1T.txt', 'r')
    print(Fore.YELLOW + 'Set1:',Fore.CYAN + set1T.read(),Fore.RED + '│ Add more words to play this set!' if len(wordCheck1) < 2 else '')
    set1T.close()
    print()

    set2T = open('pWords2T.txt', 'r')
    print(Fore.YELLOW + 'Set2:',Fore.CYAN + set2T.read(),Fore.RED + '│ Add more words to play this set!' if len(wordCheck2) < 2 else '')
    set2T.close()
    print()

    set3T = open('pWords3T.txt', 'r')
    print(Fore.YELLOW + 'Set3:',Fore.CYAN + set3T.read(),Fore.RED + '│ Add more words to play this set!' if len(wordCheck3) < 2 else '')
    set3T.close()
    print()


    set4T = open('pWords4T.txt', 'r')
    print(Fore.YELLOW + 'Set4:',Fore.CYAN + set4T.read(),Fore.RED + '│ Add more words to play this set!' if len(wordCheck4) < 2 else '')
    set4T.close()
    print()

    set5T = open('pWords5T.txt', 'r')
    print(Fore.YELLOW + 'Set5:',Fore.CYAN + set5T.read(),Fore.RED + '│ Add more words to play this set!' if len(wordCheck5) < 2 else '')
    set5T.close()
    print()


    print(Fore.BLUE + 'Enter 6 to leave')
    print()
    time.sleep(0.1)

    while True:
        try:
            flush_input()
            cSet = input(Fore.GREEN + 'Choose a set number to play or edit: ')
            if int(cSet) > 6 or int(cSet) < 1:
                cSet = int('f')
            else:
                break
        except:
            print(Fore.RED + 'This is currently unavaliable')
            print()
    
    clear()
    if cSet == '6':
        call(['python','Spelling_Game.py'])
        sys.exit()


    else:
        print(Fore.GREEN + '1) Play word list')
        print(Fore.BLUE + '2) Change title')
        print('3) Add words')
        print(Fore.RED + '4) Remove specific words')
        print('5) Clear word list and title')

        time.sleep(0.1)

        while True:
            try:
                flush_input()
                print()
                option = int(input(Fore.GREEN + 'What would you like to do: '))
                if option > 5 or option < 1:
                    option = int('f')
                break
            except:
                print(Fore.RED + 'This is currently unavaliable')

        clear()
        if option == 2:
            if cSet == '1':
                setT = open('pWords1T.txt', 'w')
            elif cSet == '2':
                setT = open('pWords2T.txt', 'w')
            elif cSet == '3':
                setT = open('pWords3T.txt', 'w')
            elif cSet == '4':
                setT = open('pWords4T.txt', 'w')
            elif cSet == '5':
                setT = open('pWords5T.txt', 'w')    

            flush_input()
            newTitle = input(Fore.GREEN + 'Enter your new title: ').title()
            setT.write(newTitle)
            setT.close()
            print()
            print(Fore.BLUE + 'Changes made!')
            time.sleep(1.2)
            clear()

        elif option == 3:
            print(Fore.GREEN + 'Words in selected list: ')
            print()
            if cSet == '1':
                wordList = open('pWords1.txt').read().splitlines()
              
                for word in wordList:
                    print(Fore.CYAN + word)
                wordList = open('pWords1.txt', 'a')

            elif cSet == '2':
                wordList = open('pWords2.txt').read().splitlines()
                
                for word in wordList:
                    print(Fore.CYAN + word)
                wordList = open('pWords2.txt', 'a')

            elif cSet == '3':
                wordList = open('pWords3.txt').read().splitlines()
               
                for word in wordList:
                    print(Fore.CYAN + word)
                wordList = open('pWords3.txt', 'a')

            elif cSet == '4':
                wordList = open('pWords4.txt').read().splitlines()
               
                for word in wordList:
                    print(Fore.CYAN + word)
                wordList = open('pWords4.txt', 'a')

            elif cSet == '5':
                wordList = open('pWords5.txt').read().splitlines()
               
                for word in wordList:
                    print(Fore.CYAN + word)
                wordList = open('pWords5.txt', 'a')

            flush_input()
            print()
            add2List = input(Fore.GREEN + 'Enter words you would like to add seperated by a single space: ').lower().split()
            for word in add2List:
                wordList.write(word)
                wordList.write('\n')

            wordList.close()
            print(Fore.MAGENTA + '\nWords added!')
            time.sleep(1.2)
            clear()
            call(['python', 'pWords.py'])
            sys.exit()

        elif option == 5:
            if cSet == '1':
                wordList = open('pWords1.txt', 'w')
                wordList = open('pWords1T.txt', 'w')
                wordList.write('Empty set')

            elif cSet == '2':
                wordList = open('pWords2.txt', 'w')
                wordList = open('pWords2T.txt', 'w')
                wordList.write('Empty set')

            elif cSet == '3':
                wordList = open('pWords3.txt', 'w')
                wordList = open('pWords3T.txt', 'w')
                wordList.write('Empty set')

            elif cSet == '4':
                wordList = open('pWords4.txt', 'w')
                wordList = open('pWords4T.txt', 'w')
                wordList.write('Empty set')

            elif cSet == '5':
                wordList = open('pWords5.txt', 'w')
                wordList = open('pWords5T.txt', 'w')
                wordList.write('Empty set')

            wordList.close()
            print(Fore.MAGENTA + 'All cleared!')
            time.sleep(1.2)
            clear()
            call(['python', 'pWords.py'])
            sys.exit()

        elif option == 4:
            if cSet == '1':
                wordList = open('pWords1.txt').read().splitlines()
            elif cSet == '2':
                wordList = open('pWords2.txt', 'r').read().splitlines()
            elif cSet == '3':
                wordList = open('pWords3.txt', 'r').read().splitlines()
            elif cSet == '4':
                wordList = open('pWords4.txt', 'r').read().splitlines()
            elif cSet == '5':
                wordList = open('pWords5.txt', 'r').read().splitlines()
    
            rWords = []
            
            print(Fore.GREEN + 'Words in selected list: ')
            print()
            for word in wordList:
                print(Fore.CYAN + word)
            flush_input()
            print()
            words2Remove = input(Fore.GREEN + 'Enter words you would like to remove seperated by a space: ').lower().split()
            for word in words2Remove:
                for cWords in wordList:
                    if word == cWords:
                        wordList.remove(cWords)
                        if cSet == '1':
                            wordListW = open('pWords1.txt', 'w')
                        elif cSet == '2':
                            wordListW = open('pWords2.txt', 'w')
                        elif cSet == '3':
                            wordListW = open('pWords3.txt', 'w')
                        elif cSet == '4':
                            wordListW = open('pWords4.txt', 'w')
                        elif cSet == '5':
                            wordListW = open('pWords5.txt', 'w')

                        for aWords in wordList:
                            wordListW.write(aWords)
                            wordListW.write('\n')
                            

                        wordListW.close()
                        print()
                        print(Fore.YELLOW + 'A word has been removed!')
                        time.sleep(0.4)
                        rWords.append(cWords)

            print(Fore.CYAN + '\nRemoved the following words:',*rWords)
            time.sleep(2.5)
            clear()


        elif option == 1:
            if cSet == '1':
                wordList = open('pWords1.txt').read().splitlines()
            elif cSet == '2':
                wordList = open('pWords2.txt', 'r').read().splitlines()
            elif cSet == '3':
                wordList = open('pWords3.txt', 'r').read().splitlines()
            elif cSet == '4':
                wordList = open('pWords4.txt', 'r').read().splitlines()
            elif cSet == '5':
                wordList = open('pWords5.txt', 'r').read().splitlines()
            
            print(Fore.GREEN + 'Words in selected list: ')
            print()
            for word in wordList:
                time.sleep(0.1)
                print(Fore.CYAN + word)

            print()
            time.sleep(0.2)
            print(Fore.GREEN + '1) Easy')
            time.sleep(0.1)
            print(Fore.YELLOW + '2) Medium')
            time.sleep(0.1)
            print(Fore.RED + '3) Hard')
            time.sleep(0.1)
            dDifficulty = open('dDifficulty.txt').read()
            if dDifficulty == '1':
                dDifficulty = 'easy'
            elif dDifficulty == '2':
                dDifficulty = 'medium'
            else:
                dDifficulty = 'hard'
            while True:
                try:
                    print(Fore.MAGENTA + 'Choose a difficulty to play or press enter to play \
on default which is currently set to:', dDifficulty)
                    difficulty = input('-> ')
                    if difficulty == '3' or difficulty == '2' or difficulty == '1' or difficulty == '':
                        break
                    else:
                        difficulty = int('f')
                except ValueError:
                    print()
                    print(Fore.RED + 'Oopsie this is either invalid or not available')

            def cDefault(difficulty):
                clear()
                print(Fore.YELLOW + '''1) Play using this difficulty
2) Set as default and play using this difficulty
''')
                while True:
                    try:
                        option = int(input(Fore.MAGENTA + 'Choose an option: '))
                        if option > 2 or option < 1:
                            option = int('f')
                        break
                    except:
                        print()
                        print(Fore.RED + 'This is invalid try again')

                if option == 1:
                    clear()
                else:
                    clear()
                    if difficulty == '1':
                        difficulty = open('dDifficulty.txt', 'w')
                        difficulty.write('1')
                        difficulty.close()
                    elif difficulty == '2':
                        difficulty = open('dDifficulty.txt', 'w')
                        difficulty.write('2')
                        difficulty.close()
                    else:
                        difficulty = open('dDifficulty.txt', 'w')
                        difficulty.write('3')
                        difficulty.close()


            if difficulty == '1':
                cDefault(difficulty)
                tLength = 0.8
            elif difficulty == '2':
                cDefault(difficulty)
                tLength = 0.3
            elif difficulty == '3':
                cDefault(difficulty)
                tLength = 0.05
            else:
                difficulty = open('dDifficulty.txt').read()
                if difficulty == '1':
                    tLength = 0.8
                elif difficulty == '2':
                    tLength = 0.3
                else:
                    tLength = 0.05

            clear()
            print(Fore.YELLOW + 'Starting', end='')
            time.sleep(0.9)
            print(' now!')
            time.sleep(0.3)


            while again == '':
                print(Fore.CYAN + '')
                clear()
                flag = False
                if cSet == '1' and len(wordCheck1) > 1: 
                    lines = open('pWords1.txt').read().splitlines()
                    randomizer = random.randint(0, len(lines)-1)

                elif cSet == '2' and len(wordCheck2) > 1: 
                    lines = open('pWords2.txt').read().splitlines() 
                    randomizer = random.randint(0, len(lines)-1)

                elif cSet == '3' and len(wordCheck3) > 1: 
                    lines = open('pWords3.txt').read().splitlines() 
                    randomizer = random.randint(0, len(lines)-1)

                elif cSet == '5' and len(wordCheck5) > 1: 
                    lines = open('pWords5.txt').read().splitlines() 
                    randomizer = random.randint(0, len(lines)-1)

                elif cSet == '4' and len(wordCheck4) > 1: 
                    lines = open('pWords4.txt').read().splitlines() 
                    randomizer = random.randint(0, len(lines)-1)

                else:
                    flag = True

                if flag == True:
                    print(Fore.RED + 'The selected list does not have enough words!')
                    time.sleep(1.75)
                    clear()
                    break

                questionV = lines[randomizer].lower()
            
                question = []
                for letter in questionV:
                    question.append(letter)

                tLength = tLength + (len(question) / 2.5)

                print(questionV)
                time.sleep(tLength)
                clear()

                    ## for input1
                print(difficulty)
                if inputM == '1':
                    print(Fore.GREEN + 'You currently have', points, 'points')
                    print(Fore.MAGENTA + '')
                    flush_input()
                    while True:
                        try:
                            answer = inputimeout(prompt = 'Spell the word: ', timeout = answeTimeout).lower()
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
                                    flush_input()
                                    aLetter = inputimeout(prompt = 'Spell the word, letter at a time: ', timeout = answeTimeout).lower()
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
                    print(Fore.MAGENTA + 'You put:', ''.join(answer))
                    print()
                    print(Fore.GREEN + 'Correct answer:',''.join(question))

                while True:
                    try:
                        flush_input()
                        again = input(Fore.YELLOW + '''\n\nPress enter to play again,
or type 'w' to go back to main screen: ''').lower()
                        if again == '' or again == 'w':
                            break
                        else:
                            again = int('f')
                    except:
                        print(Fore.RED + 'Invalid')
                clear()

                if again == 'w':
                    print(Fore.GREEN + 'Stats for this round:\n')
                    print(Fore.YELLOW + 'Total number of questions answered:', incorrect + correct)
                    print('Total points accumulated: ', points)
                    print()
                    print(str((correct / (correct + incorrect)) * 100) + '% Accuracy')
                    flush_input()
                    go = input('\nPress enter to continue: ')
                    clear()
                    call(['python', 'pWords.py'])
                    sys.exit()

print('If u see this then report a bug!')
time.sleep(99)


              

 



