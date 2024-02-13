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

def main():
    """
    Runs all the games functions.
    """
    new_game()
    game_board()

main()