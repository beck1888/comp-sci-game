# Main.py

# Imports
import os
import time
import datetime
import pygame # pygame is NEEDED for the file to run (it handles sound)

# Start helper apps
pygame.init()


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
        Thank you to freesound.org for providing the sound clips used in this project. For the more formal version of this, check out /setup/audio_credits.md

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
        # play_sound_effect('buy')
        '''Not using playsound b/c it slows it down here, only for the end'''
        # Add item to shopping cart list
        # break?
    else:
        points = points - point_penalty
        # Don't show the user point penalty, they have to infer
        print(f"UPDATE: {item} skipped")
    return money, points


def game_over(reason):
    for _ in range(10):
        print() # Create a space to show game over
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
    
def trick_question(question, game_over_note, update_when_no):
    user_choice = input(f"{question}")
    if user_choice == 'y':
        clear_console()
        play_sound_effect('game_over') 
        print(f"GAME OVER: {game_over_note}.")
        time.sleep(2)
        clear_console()
        exit()
    else:
        print(str(update_when_no))

def play_sound_effect(name):
    pygame.init() # Get ready to play the sound
    if name == 'police':
        pygame.mixer.music.load('audio/police.wav')
    elif name == 'buy':
        pygame.mixer.music.load('audio/buy.wav')
    elif name == 'game_over':
        pygame.mixer.music.load('audio/game_over.wav')
    elif name == 'game_win':
        pygame.mixer.music.load('audio/game_win.wav')
    else:
        pass #blank for now
    # Then play the sound
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    # Quit helper program when done
    pygame.quit()

# Check age function
def check_age():
    age = int(input("How old are you: "))
    if age < 12:
        years_until_allowed = 12 - age
        print(f"Sorry, but you are too young to shop alone. Come back in {years_until_allowed} years.")
        time.sleep(4)
    elif age > 999:
        print(f"No way you are {age} years old. Try again.")
        time.sleep(2)
        clear_console
        check_age()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# CODE STARTS BELOW HERE | FUNCTION DEFINITIONS ARE ABOVE
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Intro/ welcome
time.sleep(2) # Allows pygame to load
clear_console()
time.sleep(1)
give_credit()
time.sleep(1.5) # Hold credits on screen for a bit, but extend for final game
clear_console()

# Intro (w/ asking stuff)
current_time = str(datetime.datetime.now())
print(f"Welcome! The time is currently {current_time}.")
print()
print("Just a few questions before we start...")
username = input("What is your name: ")
check_age()


# Cart
if input("Do you want to get a shopping cart?: ") == 'y':
    pass
else:
    game_over("You need a shopping cart to go shopping")

# Buy things y/n
money, points = ask_to_buy('beans', 3, 1, money, points)
money, points = ask_to_buy('eggs', 5, 1, money, points)
money, points = ask_to_buy('milk', 5, 3, money, points)
money, points = ask_to_buy('bread', 4, 1, money, points)
money, points = ask_to_buy('coffee', 8, 2, money, points)
money, points = ask_to_buy('fruit', 18, 4, money, points)
money, points = ask_to_buy('veggies', 15, 2, money, points)
money, points = ask_to_buy('candy', 5, 1, money, points)
money, points = ask_to_buy('book', 15, 1, money, points)

# For testing, let's print out the money and points left
print() # Print new lines to make the end more clear
print()
print(f"Money: {str(money)}")
print(f"Points: {str(points)}")
print()
print()
time.sleep(1) # Hold the screen

# Trick question 1
trick_question("Do you want to buy an iPhone for $1,000? ", "An iPhone is out of your budget", "UPDATE: iPhone skipped")

# Validate money and points

# More trick questions if money was validated
user_choice = input("Do you want to pay for your stuff? ")
if user_choice == 'y':
    print("UPDATE: Checkout complete!")
    play_sound_effect('buy')
else:
    clear_console()
    print("GAME OVER: It is illegal to steal.")
    play_sound_effect('police')
    time.sleep(2)
    clear_console()
    exit()

user_choice = input("Do you want to drive home at 100mph? ")
if user_choice == 'n':
    print("UPDATE: You made it home safe and sound!")
else:
    clear_console()
    print("GAME OVER: You got a ticket for more than your remaining budget.")
    play_sound_effect('police')
    time.sleep(2)
    exit()

user_choice = input("Do you want to put away your purchase right away? ")
if user_choice == 'y':
    pass # Win
else:
    clear_console()
    play_sound_effect('game_win')
    print("GAME OVER: Your food went rotten.")
    time.sleep(2)
    clear_console()
    exit()

# WIN!!!
clear_console()
print(f"You have {money} dollars and {points} points left!!!")
print("You win!!! Nice job!!!")
# play win sound
time.sleep(2)
clear_console()


# Ask to pay for stuff
# Make sure enough money exists
# Drive home
# Put stuff away