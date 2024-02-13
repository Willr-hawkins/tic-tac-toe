from random import randint

def new_game():
    """
    Introduce the player to the game, ask for player name input.
    """
    print('You are now playing Tic Tac Toe!')
    print('_' * 35)
    print('This is a single player game against a computer.')
    print('_' * 35)
    player_name = input('Please enter your name:\n')


def game_board():
    """
    Creates a board for the game.
    """

    board_numbers = [1,2,3,4,5,6,7,8,9]
    board = [[1,2,3], [4,5,6], [7,8,9]]
    rows = 3
    cols = 3

    for x in range(rows):
        print('\n+---+---+---+')
        print('|', end = '')
        for y in range(cols):
            print('', board[x][y], end = ' |')
    print('\n+---+---+---+')


def update_board(num, turn):
    """
    Updates the numbers on the game board.
    checks whether the player or computer picked 
    the number.
    """
    num -= 1

    if(num == 0):
        game_board[0][0] = turn
    elif(num == 1):
        game_board[0][1] = turn
    elif(num == 2):
        game_board[0][2] = turn
    elif(num == 3):
        game_board[1][0] = turn
    elif(num == 4):
        game_board[1][1] = turn
    elif(num == 5):
        game_board[1][2] = turn
    elif(num == 6):
        game_board[2][0] = turn
    elif(num == 7):
        game_board[2][1] = turn
    elif( num == 8):
        game_board[2][2] = turn


def 


def main():
    """
    Runs all the games functions.
    """
    new_game()
    game_board()

main()