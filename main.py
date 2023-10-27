# Main.py

# Imports
import pygame # pygame is NEEDED for the file to run (it handles sound)
for _ in range(3):
    print(f"/n/n/n") # 'clears' screen

# Make some vars global
global money
global points

# Set vars
money = 50
points = 10

# Set list
#// put a 'shopping cart' list here

# Defs
def is_valid_input(input_to_check):
    print("function not written yet")

def ask_to_buy(item, cost, point_penalty):
    choice = print(f"Do you want to buy {item} for ${cost}? ")
    if choice == 'y':
        money = money - cost
        print(f"UPDATE: {item} added to cart")
        # Add item to shopping cart list
        # break?
    else:
        points = points - point_penalty
        # Don't show the user point penalty, they have to infer
        print(f"UPDATE: {item} skipped")


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

