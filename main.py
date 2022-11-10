import random
import os
from art import *
import inquirer
import time
import sys
import keyboard

def cls():
    #clears console
    os.system('cls' if os.name=='nt' else 'clear')

# clears console to initialize a blank start
cls()

# game title
gameTitleTop = """----------------------------------------------------
||||||||||||||||||||||||||||||||||||||||||||||||||||"""
gameTitleText = """|NUMBER|
|||GAME|||"""
gameTitleBottom = """||||||||||||||||||||||||||||||||||||||||||||||||||||
----------------------------------------------------\n"""

def gameTitle():
    print(gameTitleTop)
    tprint(gameTitleText, font="big")
    print(gameTitleBottom)

gameTitle()

# assigns the minimum number
minNum = 0

# loading arrow ascii
def fixedLoadingAnimation(animationTimeInterval, gameLevel):
    animationLoadingNum = 0
    # TODO: make loading time random
    if gameLevel == 0:
        # assigns random number between 0-3 as the animation loading time
        animationLoadingTime = int(random.random() * 3)
    elif gameLevel == 1:
        # assigns random number between 1-5 as the animation loading time
        animationLoadingTime = int(random.random() * 4) + 1
    elif gameLevel == 2:
        # assigns random number between 3-5 as the animation loading time
        animationLoadingTime = int(random.random() * 3) + 2

    while animationLoadingNum < 2:
        sys.stdout.write("\rloading |")
        time.sleep(animationTimeInterval)
        sys.stdout.write("\rloading /")
        time.sleep(animationTimeInterval)
        sys.stdout.write("\rloading -")
        time.sleep(animationTimeInterval)
        sys.stdout.write("\rloading \\")
        time.sleep(animationTimeInterval)
        animationLoadingNum += 1
    sys.stdout.write("\r")

# game difficulty options
gameDifficultyOptions = [
    inquirer.List("difficulty",
            message="Pick a level",
            choices=["EASY", "NORMAL", "HARD"],
    ),
]

def numberGame():
    # choose game difficulty prompt
    gameDifficultyPrompt = inquirer.prompt(gameDifficultyOptions)
    # picks a random number to guess
    if gameDifficultyPrompt == {"difficulty": "EASY"}:
        # assigns a random number between 0-10
        num = int(random.random() * 11)
        # assigns the maximum number
        maxNum = 10
        # loading animation
        fixedLoadingAnimation(0.1, 0)
    elif gameDifficultyPrompt == {"difficulty": "NORMAL"}:
        # assigns a random number between 0-100
        num = int(random.random() * 101)
        # assigns the maximum number
        maxNum = 100
        # loading animation
        fixedLoadingAnimation(0.1, 1)
    elif gameDifficultyPrompt == {"difficulty": "HARD"}:
        # assigns a random number between 0-1000
        num = int(random.random() * 1001)
        # assigns the maximum number
        maxNum = 1000
        # loading animation
        fixedLoadingAnimation(0.1, 2)
    # assigns the minimum and maximum guessed number
    lowNum = 0
    highNum = maxNum
    # restarts number of guesses to 0
    numberOfGuesses = 0
    # game input prompt
    guessInputPrompt = "Guess the number (" + str(lowNum) + " to " + str(highNum) + "):\n"
    
    # initial game prompt
    guess = input(guessInputPrompt)
    
    i = 0
    while i == 0:
        if len(guess) == 0:
            guess = input("Please enter a number between " + str(lowNum) + " to " + str(highNum) + ":\n")
        elif guess.isdigit() == False or int(guess) < minNum or int(guess) > maxNum:
            guess = input("Only numbers between 0 to " + str(maxNum) + " are allowed, try again:\n")
        elif int(guess) == num or int(guess) == num - 1 and highNum == num or int(guess) == num + 1 and lowNum == num: #lowNum == num and highNum == num:
            # stops game
            i =+ 1
            # play again loop
            j = 0;
            while j == 0:
                # play again prompt
                playAgain = input("\n----------------------------------------------------\n" + str(num) + " is the correct number!\nYou won after " + str(numberOfGuesses + 1) + " guesses\nPlay again?[Y/n]")
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
                    # game title
                    gameTitle()
                    prompt = input("Thank you for playing!\nIf at any time you would like to continue,\npress the enter key on your keyboard\n")
                    numberGame()
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
        numberOfGuesses += 1

# initial game ran
numberGame()