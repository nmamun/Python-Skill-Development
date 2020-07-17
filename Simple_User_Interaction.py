#!/usr/bin/env python

# ==============================================================
__author__ = "Nurul Mamun"
__date__ = " 13 July, 2020"
__version__ = "1.0"
__description__ = """Simple User Interaction - display information to user, accept input from user, 
                     validate user input, update information based on user input"""
# ==============================================================

# ========== Imports ===========================================

# ==============================================================

# ========= Functions ==========================================

# Display the game object
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

# User chooses a position
def position_choice():

    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input("Pick a postion (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice ! ")
    
    return int(choice)

# Replace the position with choice 
def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

# Continue game choice
def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y','N']:
        choice = input("Keep playing? ( Y or N): ")
        if choice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N ")
    if choice == 'Y':
        return True
    else:
        return False
  
# ==============================================================

# ========== Main Function =====================================
def main():
    game_list = ['0','1','2']
    game_on = True

    while game_on == True:
        display_game(game_list)
        position = position_choice()
        game_list = replacement_choice(game_list,position)
        display_game(game_list)
        game_on = gameon_choice()

# ==============================================================


if __name__ == "__main__":
    main()