# Main.py

# Imports
import pygame # pygame is NEEDED for the file to run (it handles sound)
print("Hello world")

# Make some vars global
global money
global points

# Set vars
money = 50
points = 10

# Defs
def is_valid_input(input_to_check):
    print()

def game_over(reason):
    for _ in range(10):
        print()
    print(f"GAME OVER: {reason}.")
    exit()

def update_point(subtract):
    points = points - subtract
    if points < 0:
        game_over("You've run out of points!")
    else:
        return

def update_money(subtraction):
    money = money - subtraction
    if money < 0:
        game_over("You've run out of money!")
    else:
        return

# Intro/ welcome
print("For now, just type y or n for each question")

# Code/game
# Cart
if input("Do you want to get a shopping cart?: ") == 'y':
    pass
else:
    game_over("You need a shopping cart to go shopping")