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




def main():
    """
    Runs all the games functions.
    """
    new_game()
    game_board()

main()