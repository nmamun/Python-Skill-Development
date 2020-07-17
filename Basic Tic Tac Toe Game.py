#!/usr/bin/env python

# ==============================================================
__author__ = "Nurul Mamun"
__date__ = " 13 July, 2020"
__version__ = "1.0"
__description__ = """ A Basic Tic Tac Toe Game - interacting with 02 players,
                        display board, take input from player, validate, 
                        display updated board, choose winner"""
# ==============================================================

# ========== Imports ===========================================
import random
# ==============================================================

# ========= Functions ==========================================
# Display Tic Tac Toe board
def display_board(board):
    print('\n'*50)
    print('+---+---+---+')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('+---+---+---+')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('+---+---+---+')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print('+---+---+---+')
    return board

# Decide which player will be asked to choose symbol (random selection)
def choose_player_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Symbol choice for Player 1, Player 2 will be assigned the other symbol
def player_choice_input():
    
    player_1_choice = ''

    while player_1_choice not in ['X','O']:
        player_1_choice = input("Player 1: Do you want to be X or O ? ").upper()
        if player_1_choice not in ['X','O']:
            print("Sorry, please choose X or O !")
    

    if player_1_choice == 'X':
        player_2_choice = 'O'
    else:
        player_2_choice = 'X'

    print(f"Player 1 Symbol - {player_1_choice}")
    print(f"Player 2 Symbol - {player_2_choice}")

    return (player_1_choice,player_2_choice)

# Prepare the board with right symbol, position
def place_marker(board,marker,position):
    board[position] = marker
    return board

# Winner check
def win_check(board,marker):
    return ((board[7] == board[8] == board[9] == marker) or # Horizontal top row
            (board[4] == board[5] == board[6] == marker) or # Horizontal middle row
            (board[1] == board[2] == board[3] == marker) or # Horizontal bottom row

            (board[7] == board[4] == board[1] == marker) or # Vertical first column
            (board[8] == board[5] == board[2] == marker) or # Vertical second column
            (board[9] == board[6] == board[3] == marker) or # Vertical third column

            (board[7] == board[5] == board[3] == marker) or # diagonal
            (board[9] == board[5] == board[1] == marker))

# Check if a space in the board is available
def space_check(board,position):
    return board[position] == ' '

# Check if the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Ask player to choose position to fill out with a symbol and validate if that selection is a numeric,
# within acceptable range and the space is available
def player_position_choice(board):
    position = 'wrong'
    acceptable_value = range(1,10)
    within_range = False

    # Conditions check
    while position.isdigit() == False or within_range == False:
        position = input("Choose your next position: (1-9): ")

        # Digit check
        if position.isdigit() == False:
            print("Sorry, that is not a digit")
        
        # Range check
        if position.isdigit() == True:
            if int(position) in acceptable_value:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (1-9)")
                within_range = False
        
        # Space check
        if position.isdigit() == True and within_range == True:
            position_1 = int(position)
            if not space_check(board, position_1):
                print("Sorry, that choice is not available")
                position = input("Choose your next position: (1-9): ")

    return int(position)

# Asking player if they want to continue
def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')
# ==============================================================

# ========== Main Function =====================================
def main():
    print("Welcome to Tic Tac Toe !")
    
    while True:
        # Setup the board
        ttt_board = [' '] * 10
        # Select symbol for both players
        player_1_choice,player_2_choice = player_choice_input()
        # Select which player will be first & prompt
        turn = choose_player_first()
        print(turn + ' will go first.')

        # Prompt to start
        play_game = input("Are you ready to play? Enter Yes or No: ")

        # Assign variable to keep the game playing
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
        
        while game_on:
            if turn == 'Player 1':
                # Player 1's turn
                # Show the board
                display_board(ttt_board)
                print("Player 1's turn => ")
                # Ask for the position to fill up
                position = player_position_choice(ttt_board)
                # Update the board with player's asked position
                place_marker(ttt_board, player_1_choice, position)

                # Check if player 1 has won - any win combination met
                if win_check(ttt_board, player_1_choice):
                    display_board(ttt_board)
                    print("Congratulations! Player 1 has won the game !")
                    # break out of 'while' loop if win combination met
                    game_on = False
                    
                # No win combination met, check if there is space available in the board
                else:
                    if full_board_check(ttt_board):
                        display_board(ttt_board)
                        print("The game is a draw !")
                        break
                    else:
                        # No win combination met & board is not full, then go for player 2
                        turn = 'Player 2'
            else:
                # Player 2's turn
                display_board(ttt_board)
                # Show the board
                print("Player 2's turn =>")
                # Ask for the position to fill up
                position = player_position_choice(ttt_board)
                # Update the board with player's asked position
                place_marker(ttt_board, player_2_choice, position)

                # Check if player 2 has won - any win combination met
                if win_check(ttt_board, player_2_choice):
                    display_board(ttt_board)
                    print("Congratulations! Player 2 has won the game !")
                    # break out of 'while' loop if win combination met
                    game_on = False
                else:
                    # No win combination met, check if there is space available in the board
                    if full_board_check(ttt_board):
                        display_board(ttt_board)
                        print("The game is a draw !")
                        break
                    else:
                        # No win combination met & board is not full, then go for player 1
                        turn = 'Player 1'
        if not replay():
            break

# ==============================================================


if __name__ == "__main__":
    main()