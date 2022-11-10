import random
import os
from art import *
import inquirer
import time
import sys

def cls():
    #clears console
    os.system('cls' if os.name=='nt' else 'clear')

# clears console to initialize a blank start
cls()

# game title
gameTitleText = """NUMBER
     GAME"""
tprint("""------
NUMBER
     GAME
------""", font="big")

# animation time interval
animationTimeInterval = 1

# loading arrow ascii
def arrowAnimationFourSeconds():
    initialLoad = 0
    while initialLoad < 2:
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                   ______
                   \    /
                    \  /
                     \/ """)
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                      |\ 
                      | \ 
                      |  \ 
                      |___\ """)
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                     /|
                    / |
                    \ |
                     \|""")
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                     ____
                     |  /
                     | /
                     |/""")
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                       /\ 
                      / \ 
                     /   \ 
                    /_____\ """)
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                     ____
                     \  |
                      \ |
                       \|""")
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                       |\ 
                       | \ 
                       | /
                       |/""")
        time.sleep(animationTimeInterval)
        cls()
        tprint(gameTitleText, font="big")
        sys.stdout.write("""                        /|
                       / |
                      /  |
                     /___|""")
        initialLoad += 1
        time.sleep(animationTimeInterval)
    cls()

time.sleep(3)
arrowAnimationFourSeconds()

def numberGame():
    # choose game difficulty prompt
    gameDifficultyOptions = [
        inquirer.List("difficulty",
                message="Pick a level",
                choices=["EASY", "NORMAL", "HARD"],
        ),
    ]
    gameDifficultyPrompt = inquirer.prompt(gameDifficultyOptions)
    # picks a random number to guess
    if gameDifficultyPrompt == {"difficulty": "EASY"}:
        # assigns a random number between 0-10
        num = int(random.random() * 11)
        # assigns the maximum number
        maxNum = 10
    elif gameDifficultyPrompt == {"difficulty": "NORMAL"}:
        # assigns a random number between 0-100
        num = int(random.random() * 101)
        # assigns the maximum number
        maxNum = 100
    elif gameDifficultyPrompt == {"difficulty": "HARD"}:
        # assigns a random number between 0-1000
        num = int(random.random() * 1001)
        # assigns the maximum number
        maxNum = 1000
    # assigns the minimum and maximum guessed number
    lowNum = 0
    highNum = maxNum
    # game prompts
    guessInputPrompt = "Guess the number (" + str(lowNum) + " to " + str(highNum) + "):\n"
    playAgainInputPrompt = str(num) + " is the correct number! Play again?[Y/n]"
    # initial game prompt
    guess = input(guessInputPrompt)
    
    i = 0
    while i == 0:
        if len(guess) == 0:
            guess = input("Please enter a number between " + str(lowNum) + " to " + str(highNum) + ":\n")
        elif guess.isdigit() == False:
            guess = input("Only numbers are allowed, try again:\n")
        elif int(guess) < lowNum or int(guess) > maxNum:
            guess = input("Only numbers between 0 to " + str(maxNum) + ", try again:\n")
        elif int(guess) == num or int(guess) == num - 1 and highNum == num or int(guess) == num + 1 and lowNum == num: #lowNum == num and highNum == num:
            # stops game
            i =+ 1
            # play again loop
            j = 0;
            while j == 0:
                # play again prompt
                playAgain = input(playAgainInputPrompt)
                if str(playAgain).isalpha() == False and len(playAgain) > 0:
                    # play again prompt
                    j = 0
                elif playAgain.lower() == "y" or playAgain.lower() == "yes" or len(playAgain) == 0:
                    # stops play again loop
                    j = 1
                    # clears console
                    cls()
                    # restarts the game
                    numberGame()
                elif playAgain.lower() == "n" or playAgain.lower() == "no":
                    # stops play again loop
                    j = 1
                    # clears console
                    cls()
                    print("Thank you for playing!")
        elif int(guess) <= num and int(guess) >= lowNum:
            lowNum = int(guess) + 1
            guess = input("Too low of a guess, try again (" + str(lowNum) + " to " + str(highNum) + "):\n")
        elif int(guess) <= num:
            guess = input("Too low of a guess, try again (" + str(lowNum) + " to " + str(highNum) + "):\n")
        elif int(guess) >= num and int(guess) <= highNum:
            highNum = int(guess) - 1
            guess = input("Too high of a guess, try again (" + str(lowNum) + " to " + str(highNum) + "):\n")
        elif int(guess) >= num:
            guess = input("Too high of a guess, try again (" + str(lowNum) + " to " + str(highNum) + "):\n")
        else:
            print("Error, try again!")

# initial game ran
numberGame()