from multiprocessing.connection import answer_challenge
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

inputM = open('inputM.txt', 'r')
inputM = inputM.read()

if inputM == '2':
    inputM = 'Memorise'
elif inputM == '1':
    inputM = 'Natural'

wordsC = open('completion.txt').read().splitlines()



clear()
print(Fore.RED + 'Please make sure that you have read howToPlay and reviewed your settings before playing.\n\n')


while True:
    print(Fore.GREEN + '''Easy levels:
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬''')
    print('1) Wild animals' , Fore.GREEN + ' -completed!' if wordsC[0] == '1' else Fore.RED + ' -incomplete'\
, Fore.BLUE + ' ---------> Input method used:', inputM)  
    print(Fore.GREEN + '2) Electronics' , Fore.GREEN + '  -completed!' if wordsC[1] == '1' else Fore.RED + '  -incomplete'\
, Fore.BLUE + ' ---------> Input method used:', inputM) 
    time.sleep(0.1)
    print(Fore.YELLOW + '''\n
Medium levels:
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬''')
    print('3) Oceanic creatures' , Fore.GREEN + ' -completed!' if wordsC[2] == '1' else Fore.RED + ' -incomplete'\
, Fore.BLUE + ' ---------> Input method used: Natural') 
    print(Fore.YELLOW + '4) Food' , Fore.GREEN + '              -completed!' if wordsC[3] == '1' else\
         Fore.RED + '              -incomplete'\
, Fore.BLUE + ' ---------> Input method used: Memorise') 
    time.sleep(0.1)
    print(Fore.RED + '''\n
Hard levels:
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬''')
    print('5) Geology' , Fore.GREEN + '        -completed!' if wordsC[4] == '1' else Fore.RED + '        -incomplete'\
, Fore.BLUE + ' ---------> Input method used: Natural') 
    print(Fore.RED + '6) The Atmosphere' , Fore.GREEN + ' -completed!' if wordsC[5] == '1' else Fore.RED + ' -incomplete'\
, Fore.BLUE + ' ---------> Input method used: Memorise') 

    print(Fore.CYAN + '\nNote: Sets above easy may contain more than one word per question')
    time.sleep(0.1)

    print(Fore.BLUE + '''
Enter 'l' to leave''')

    print(Fore.MAGENTA + '\n\nChoose a level to play: ')
    while True:
        flush_input()
        if keyboard.is_pressed('1'):
            wLevel = 1
            break
        elif keyboard.is_pressed('2'):
            wLevel = 2
            break
        elif keyboard.is_pressed('3'):
            wLevel = 3
            break
        elif keyboard.is_pressed('4'):
            wLevel = 4
            break
        elif keyboard.is_pressed('5'):
            wLevel = 5
            break
        elif keyboard.is_pressed('6'):
            wLevel = 6
            break
        elif keyboard.is_pressed('l'):
            clear()
            call(['python', 'classicMode.py'])
            sys.exit()

    clear()
    print(Fore.YELLOW + 'Starting', end='')
    time.sleep(0.9)
    print(' now!')
    time.sleep(0.3)
    clear()
    word = 0
    if wLevel == 1: ## Wild animals
        words = '''monkey Panda Shark Zebra Gorilla Walrus Leopard Wolf eagle
Jellyfish Crab Giraffe Camel Starfish Koala Alligator Owl Tiger Bear whale'''.split()
        bTLength = 0.8
        answerTimeout = 5
        indexR = 0
        tWords = '20'

    elif wLevel == 2: ## Electronics
        words = '''clock charger counter Blender speaker Bulb fan dryer Computer
Copier camera Drill Earphones Fan Fax lamp Headset iPod Juicer Monitor'''.split()
        bTLength = 0.8
        answerTimeout = 2
        indexR = 1
        tWords = '20'

    elif wLevel == 3: ## Oceanic creatures
        words = '''Anglerfish_Barreleye Fish_Beluga Whale_Blue Glaucus_Blue ringed Octopus
_Bonnethead Shark_Bottlenose Dolphin_Dugong_Dumbo Octopus_Giant Isopod_Granrojo Jellyfish
_Great Auk_Lanternshark_Leafy Sea Dragon_Leopard Shark_Lizardfish_Megalodon_Megamouth Shark
_Mimic Octopus_Needlefish'''.split('_')
        bTLength = 0.6
        answerTimeout = 4
        indexR = 2
        tWords = '20'
        inputM = '1'

    elif wLevel == 4: ## Food
        words = '''Pumpkin Pie_Chicken Pot Pie_Alfredo Sauce_Ice Cream Cake_Cheesecake
_Banana Bread_Burritos_Chimichanga_Enchilada_Marinara Sauce_Broccoli_Chicken Tenders
_Grilled Chicken_Fried Chicken_Roasted Chicken_Mashed Potatoes_Submarine Sandwiches
_Lamb Chops_Teriyaki_Ravioli_Gelatin_Gyro Sandwhich_Chicken Nuggets_Green Bean Casserole
_Cantalope_Fried Zucchini_Calzone'''.split('_')
        bTLength = 0.6
        answerTimeout = 3
        indexR = 3
        tWords = '27'
        inputM = '2'

    elif wLevel == 5: ##Geology
        words = '''aftershock aluminum aquifer bedrock bulge caldera cataclysm decomposition deposit
depression disintegration igneous limestone lithosphere magma magnitude metamorphic sedimentary seismology
stratigraphy'''.split()
        bTLength = 0
        answerTimeout = 2.5
        indexR = 4
        tWords = '20'
        inputM = '1'
    
    elif wLevel == 6:
        words = '''atmosphere_climate_exosphere_ionosphere_jet stream_mesosphere_ozone_polar zone_stratosphere
thermosphere_tropical zone_troposphere_weather_air mass_barometer_cold front_conduction_convection_occluded front
radiation_warm front_anemometer_doldrums_horse latitude_sea breeze_wind vane_anticyclone_blizzard_cirrus_cloud
cumulonimbus_cumulus_precipitation_saturated'''.split('_')
        bTLength = 0
        answerTimeout = 1
        indexR = 5
        tWords = '31'
        inputM = '2'
    

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
                    print(Fore.GREEN + 'Spell the word: ---------------------', Fore.CYAN + str(int(answerTimeout)) \
,Fore.GREEN + 'seconds (1sf) to answer!\n')
                    answer = inputimeout(prompt = '-> ', timeout = answerTimeout + (len(question) / 6)).lower()
                    break
                except TimeoutOccurred:
                    answer = 'Oops you timed out! Maybe try an easier level first.'
                    break

        else:
            answer = []
            flag = False
            x = 0
            for letter in questionV:
                lLetter = []
                spaceCheck = question[x]
                x += 1
            ##for input 2
                if flag == False:
                    while True:
                        try:
                            clear()
                            if spaceCheck == ' ':
                                answer.append(' ')
                                break
                            lLetter = []
                            print(Fore.MAGENTA + '')
                            clear()
                            print(''.join(answer))
                            print(Fore.GREEN + 'Spell the word, letter at a time: --------', Fore.CYAN + str(int(answerTimeout)) \
,Fore.GREEN + 'seconds (1sf) to answer!\n')
                            flush_input()
                            aLetter = inputimeout(prompt = '-> ', timeout = answerTimeout).lower()
                            for l in aLetter:
                                lLetter.append(l)
                            if len(lLetter) == 1:
                                answer.append(aLetter)
                                break
                            else:
                                aLetter = int('f')

                        except TimeoutOccurred:
                            flag = True
                            answer = 'Oops you timed out! Maybe try an easier level first.'
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
            flush_input()
            print(Fore.MAGENTA + '\nPress enter to continue:')
            keyboard.wait('enter')
            call(['python', 'pLevels.py'])
            exit()

        clear()
        word += 1
    
    if word == len(words):
        print(Fore.GREEN + 'Congrats, you beat this level!\n')
        time.sleep(1)
        flush_input()
        print(Fore.MAGENTA + '\nPress enter to continue:')
        keyboard.wait('enter')
        
        wordsC[indexR] = '1'
        completion = open('completion.txt','w')
        for level in wordsC:
            completion.write(level)
            completion.write('\n')
        completion.close()

        call(['python', 'pLevels.py'])
        exit()
        