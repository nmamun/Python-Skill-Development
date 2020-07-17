#!/usr/bin/env python

# ==============================================================
__author__ = "Nurul Mamun"
__date__ = " 08 July, 2020"
__version__ = "1.0"
__description__ = " Three Cup Monte Game"
# ==============================================================

# ==========Imports=============================================
from random import shuffle
# ==============================================================

# =========Functions============================================

# Function to randomly shuffle a list and return


def shuffle_a_list(provided_list):
    shuffle(provided_list)
    return provided_list

# Function to take the input from player/user


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number between 0 - 2 : ")
    return int(guess)

# Function to validate if player/user guess is same as shuffled position


def check_guess_position(provided_list, guess):
    if provided_list[guess] == 'O':
        print("Correct ! You found the right CUP with the ball.")
    else:
        print("Wrong ! This is not the right CUP.")
# ==============================================================

# ========== Main Function =====================================


def main():
    print("""
    This is a simple approximation of 'Three Cup Monte' Game.
    A ball is hidden under one of three cups (resembled using a list of 3 items).
    List is shuffled afterwards to depict cups shuffling.
    Player/User has to guess under which cup position the ball is hidden.
    """)
    provided_list = [' ', 'O', ' ']
    shuffled_list = shuffle_a_list(provided_list)
    guess = player_guess()
    check_guess_position(shuffled_list, guess)

# ==============================================================


if __name__ == "__main__":
    main()
