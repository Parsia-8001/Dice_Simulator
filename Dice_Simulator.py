''' Parsia Bahrami - Dice Simulator '''

from time import sleep
from termcolor import colored
import random
import sys

def typer(words):
    for char in words:
        if char == ".":
            sleep(0.6)
            sys.stdout.write(char)
            sys.stdout.flush()
        else:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()


def result(number):
    sleep(0.25)
    print("Rolling the dice", end="")
    typer("...\n\n")
    sleep(1)
    print("The value is:")
    sleep(1)
    print(random.randint(1, number))
    sleep(1)
    again()


def roll():
    roll_dice = input("Select the type of dice (4, 6, 12, 18 sided): ")
    while True:  # roll_dice is 4, 6, 12, 18 sided
        try:
            if roll_dice == "4":
                number = 4
                result(number)
            if roll_dice == "6":
                number = 6
                result(number)
            elif roll_dice == "12":
                number = 12
                result(number)
            elif roll_dice == "18":
                number = 18
                result(number)
            elif roll_dice == "exit" or roll_dice == "quit":
                print("\n")
                startup()
            else:
                print("Invalid input!")
                roll()
        except ValueError:
            print("Invalid input!")


def again():
    roll_again = str.lower(input("Roll again?(Y/N) "))
    while True:
        try:
            if roll_again == "y":
                print("\n")
                sleep(1)
                roll()
            elif roll_again == "n":
                sleep(1)
                sys.exit()
            else:
                print("Invalid input!")
                again()
        except(ValueError):
            print("Invalid input!")
            again()


def startup():
    typer(colored(" 1) Start \n", "green"))
    typer(colored(" 2) Exit  \n\n", "red"))
    begin = str.lower(input(""))
    while True:
        try:
            if begin == ("1") or begin == ("start"):
                print("\n")
                roll()
            elif begin == ("2") or begin == ("exit"):
                sys.exit()
            else:
                print("Invalid input!")
                startup()
        except(ValueError):
            print("Invalid input!")


print(colored("Welcome to Dice_Simulator! Created by Parsia B.\n", "white", attrs=["bold"]))
sleep(0.5)
startup()