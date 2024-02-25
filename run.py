# Imports for libaries
import random
from art import *
import colorama
from colorama import Fore

# Automatically reset the color.
colorama.init(autoreset=True)

# Global variables:
board_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3
player_turn = (Fore.BLUE + 'X')
computer_turn = (Fore.LIGHTMAGENTA_EX + 'O')
winnerP = (Fore.GREEN + '\nWell Done! The player won.\n')
winnerC = (Fore.RED + '\nUnlucky! The computer won.\n')


def new_game():
    """
    Introduce the player to the game, ask for player name input.
    """
    Art = text2art('Tic Tac Toe')
    print(Art)
    print('_' * 35)
    print('\nThis is a single player game against a computer.\n')
    print('_' * 35)

    while True:
        player_name = input('\nPlease enter your name:\n')

        if player_name == '':
                print(Fore.RED + 'INVALID: You cannot leave name blank!')
                player_name = input('\nPlease enter your name:\n')

        try:
            player_name == int(player_name)
            print(Fore.RED + '\nINVALID: You cannot input numbers!')
            print()

        except ValueError:
            print(f'\nThe players name is {player_name}')
            break
    
    if player_name == '':
        print(Fore.RED + 'INVALID: You cannot leave name blank!')
        player_name = input('\nPlease enter your name:\n')


def game_board():
    """
    Creates a board for the game.
    """
    for x in range(rows):
        print('\n+---+---+---+')
        print('|', end='')
        for y in range(cols):
            print('', board[x][y], end=' |')
    print('\n+---+---+---+')


def update_board(num, turn):
    """
    Updates the numbers on the game board.
    checks whether the player or computer picked
    the number.
    """
    num -= 1

    if (num == 0):
        board[0][0] = turn
    elif (num == 1):
        board[0][1] = turn
    elif (num == 2):
        board[0][2] = turn
    elif (num == 3):
        board[1][0] = turn
    elif (num == 4):
        board[1][1] = turn
    elif (num == 5):
        board[1][2] = turn
    elif (num == 6):
        board[2][0] = turn
    elif (num == 7):
        board[2][1] = turn
    elif (num == 8):
        board[2][2] = turn


def check_winner(board):
    """
    Checks all ways either the player or computer could win.
    And whether it is the player or computer that wins, or if
    there is no winner.
    """
    # Checks x axis for winner
    if (board[0][0] == player_turn
            and board[0][1] == player_turn
            and board[0][2] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[0][0] == computer_turn
            and board[0][1] == computer_turn
            and board[0][2] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    elif (board[1][0] == player_turn
            and board[1][1] == player_turn
            and board[1][2] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[1][0] == computer_turn
            and board[1][1] == computer_turn
            and board[1][2] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    elif (board[2][0] == player_turn
            and board[2][1] == player_turn
            and board[2][2] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[2][0] == computer_turn
            and board[2][1] == computer_turn
            and board[2][2] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    # Checks y axis for winner
    elif (board[0][0] == player_turn
            and board[1][0] == player_turn
            and board[2][0] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[0][0] == computer_turn
            and board[1][0] == computer_turn
            and board[2][0] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    elif (board[0][1] == player_turn
            and board[1][1] == player_turn
            and board[2][1] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[0][1] == computer_turn
            and board[1][1] == computer_turn
            and board[2][1] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    elif (board[0][2] == player_turn
            and board[1][2] == player_turn
            and board[2][2] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[0][2] == computer_turn
            and board[1][2] == computer_turn
            and board[2][2] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    # check diagonals for winner
    elif (board[0][0] == player_turn
            and board[1][1] == player_turn
            and board[2][2] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[0][0] == computer_turn
            and board[1][1] == computer_turn
            and board[2][2] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    elif (board[2][0] == player_turn
            and board[1][1] == player_turn
            and board[0][2] == player_turn):
        print(winnerP)
        print('_' * 35)
        return player_turn
    elif (board[2][0] == computer_turn
            and board[1][1] == computer_turn
            and board[0][2] == computer_turn):
        print(winnerC)
        print('_' * 35)
        return computer_turn
    # No winner
    else:
        return 'N'


def get_board_values():
    """
    Gets the value for the number on the board,
    Whether it is 'X' (players turn) or 'O' (computers turn).
    """
    end_game = False
    turn_number = 0

    while end_game is False:

        if (turn_number % 2 == 0):
            game_board()

            # Validate the players input.
            player_choice = input('\nPlease choose a number between 1 - 9:\n')

            if player_choice == '':
               print(
                   Fore.RED + '\nINVALID: You cannot leave this input blank!\n'
                   )
               player_choice = input(
                    '\nPlease choose a number between 1 - 9:\n'
                    ) 

            while player_choice not in str(board_numbers):
                print(Fore.RED + '\nINVALID: please pick again!')
                player_choice = input(
                    '\nPlease choose a number between 1 - 9:\n'
                    )

            # Changes the user input into a integer.
            player_position = int(player_choice)

            print('_' * 35)
            update_board(player_position, player_turn)
            board_numbers.remove(player_position)
            turn_number += 1
        else:
            while (True):
                computer_choice = random.choice(board_numbers)
                print(f'\n{computer_choice} was picked by the computer.\n')
                print('_' * 35)
                if (computer_choice in board_numbers):
                    update_board(computer_choice, computer_turn)
                    board_numbers.remove(computer_choice)
                    turn_number += 1
                    break

        # Ends the game once there is a winner
        winner = check_winner(board)
        if (winner != 'N'):
            print('\nGame Over! Thank you for playing!\n')
            break


def main():
    """
    Runs all the games functions.
    """
    new_game()
    check_winner(board)
    get_board_values()


main()
