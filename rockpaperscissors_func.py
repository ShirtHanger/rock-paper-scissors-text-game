import random
from rockpaperscissors_lists import *

'''All functions are located here'''


def rps_computer_choice():

    """Sets computer play using list of valid options in lists file"""
    
    computer_play = random.choice(play_options)
    return computer_play


def fix_user_shortcut(user_play):

    """Properly sets user input if they chose to only input one letter (R/P/S)"""

    list_index = 0
    
    for option in user_shortcut_options:
        if user_play == option:
            user_play = play_options[list_index]
        else:
            list_index += 1
            
    return user_play


def rps_win_condition(computer_play, user_play, player_won):  # See line 6 in main for why player_won is here

    """Determines if the player or computer won"""
    """Rerolls computer play and user input if they made the same play"""

    # Prints out user and computer play
    print("You chose: " + user_play)
    print("The machine chose: " + computer_play)

    # if they are the same, re roll computer play and request another play from user.
    while computer_play == user_play:
        
        computer_play = rps_computer_choice()
        print("Looks like you made the same choice...")
        user_play = input("Again! ").lower()
        while user_play not in user_options:
            user_play = input("You should know the choices by now: ").lower()
        fix_user_shortcut(user_play)
        print("You chose: " + user_play)
        print("The machine chose: " + computer_play)

    # Determines winner
    # Note to self: See if you can split this into a different function in future

    if computer_play == "rock":
        if user_play == "paper":
            player_won = True
        else:  # The user play was scissors
            player_won = False

    if computer_play == "paper":
        if user_play == "rock":
            player_won = False
        else:  # The user play was scissors
            player_won = True
        
    if computer_play == "scissors":
        if user_play == "rock":
            player_won = True
        else:  # The user play was paper
            player_won = False

    # Returns boolean to determine winner

    return player_won
