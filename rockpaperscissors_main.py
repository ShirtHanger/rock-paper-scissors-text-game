from rockpaperscissors_func import *
from rockpaperscissors_lists import *

'''All user input goes here to run text game'''

# IDK why, but I get a Scope error when the rps_win_condition function runs. Unless I have this AND make it an
# argument/parameter. Will solve in future
player_won = True

print("--------------")

print("Ready to play Rock Paper Scissors?")

# Prompts user to begin or end program
confirm = input("(QUIT) or (PLAY)? (Q/P): ").lower()
while confirm not in program_start_validation:
    confirm = input("Invalid, quit or play?: ").lower()

# Loops until user quits at end of game
while confirm in play_validation:

    print("--------------")

    # Rolls random computer play
    computer_play = rps_computer_choice()
    # Takes in user play
    user_play = input("Rock, Paper, or Scissors? (R/P/S): ").lower()
    while user_play not in user_options:
        user_play = input("Invalid option, Rock, Paper, or Scissors?: ").lower()

    # If they chose a 1 letter input (R/P/S), this code fixes it back to the full word
    if user_play in user_shortcut_options:
        user_play = fix_user_shortcut(user_play)

    print("--------------")
    # Determines winner (See line 6 for why player_won is here)
    player_won = rps_win_condition(computer_play, user_play, player_won)
    print("--------------")

    # Tells user if they won or lost
    if player_won:
        print("You win!")
    else:
        print("You lost...")

    # Asks user if they want to play again, Quits program if they say no
    confirm = input("Keep (play)ing or (quit) (Q/P)?: ")
    while confirm not in program_start_validation:
        confirm = input("Invalid, quit or play?: ").lower()

if confirm in quit_validation:
    print("Aight man, smell you later")
