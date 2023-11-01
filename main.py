# Main.py

# Imports
import os
import time
import pygame # pygame is NEEDED for the file to run (it handles sound)


# Make some vars global
global money
global points

# Set vars
money = 50
points = 10

# Set list
#// put a 'shopping cart' list here

# Def functions
def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def give_credit():
    print(
        '''CREDITS:
        Thank you to freesound.org for providing the sound clips used in this project.

        > buy.wav [Creative Commons 0] ... https://freesound.org/people/CapsLok/sounds/184438/ 
        > game_over.wav [Creative Commons 4.0] ... https://freesound.org/people/Doctor_Jekyll/sounds/240195/ (shortened in QuickTime)
        > game_win.wav [Creative Commons 0] ... original from https://freesound.org/people/EVRetro/sounds/495005/
        > police.wav [Creative Commons 0] ... https://freesound.org/people/guitarguy1985/sounds/70938/
        '''
    )

def is_valid_input(input_to_check):
    print("function not written yet")

def ask_to_buy(item, cost, point_penalty, money, points):
    choice = input(f"Do you want to buy {item} for ${cost}? ")
    if choice == 'y':
        money = money - cost # use return values
        print(f"UPDATE: {item} added to cart")
        # Add item to shopping cart list
        # break?
    else:
        points = points - point_penalty
        # Don't show the user point penalty, they have to infer
        print(f"UPDATE: {item} skipped")
    return money, points


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

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Intro/ welcome
time.sleep(1) # Allows pygame to load
clear_console()
give_credit()
time.sleep(3) # Hold credits on screen for a bit
clear_console()
print("For now, just type y or n for each question")


# Code/game

# Cart
if input("Do you want to get a shopping cart?: ") == 'y':
    pass
else:
    game_over("You need a shopping cart to go shopping")

# Buy things y/n
money, points = ask_to_buy('beans', 3, 1, money, points)
ask_to_buy('eggs', 5, 1)
ask_to_buy('milk', 5, 3)
ask_to_buy('bread', 4, 1)
ask_to_buy('coffee', 8, 2)
ask_to_buy('fruit', 18, 4)
ask_to_buy('veggies', 15, 2)
ask_to_buy('candy', 5, 1)
ask_to_buy('book', 15, 1)

# iPhone trick question
buy_iphone = input("Do you want to buy an iPhone for $1,000?")
if buy_iphone == 'y':
    pass
    # game over
else:
    pass

# Ask to pay for stuff
# Make sure enough money exists
# Drive home
# Put stuff away