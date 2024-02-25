# Tic Tac Toe 

Tic Tac Toe is a Python game that runs in the terminal, for this game it runs in the Code Institute mock terminal on Heroku.

Users of this game will try and beat the computer by getting three 'X' in a row on the board generated.

[The live link of this project is here!](https://will-tic-tac-toe-d058da233205.herokuapp.com/)

![Mockup](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/1bd14d64-287d-4c08-963d-e20071213091)

## How to play

The Tic Tac Toe project is based of the simple game many played as a kid. [Here](https://en.wikipedia.org/wiki/Tic-tac-toe) you can read more about the classic game.

In this version the player will be asked to enter their name, once entered the game baord will be displayed.

The player can then choose a position on the board which will be displayed with 'X'.

Then the computer will pick a positon at random and will be displayed with a 'O'.

The player and computer will take it in turn until either player gets 3 positions in a row and wins the game.

## Features

### Exsisting Features

- __Game Board Generation__

    - Once the player enters their name a game baord will be generated.

![GameBoard](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/5ff15a89-0ee2-4d8a-82f8-5492d43fb87d)

- __Game Play__

    - Player will play against a computer.
    - The game accepts user input.
    - Updates the game board to keep up with the 'Score'.

![GamePlay](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/f32e0f58-3cd1-4b40-8b0a-5207867b42be)

- __Input Validation__

    - You cannot enter a number as the player name.
    - You cannot pick a number that is not between 1 - 9.
    - You cannot pick a number that is already taken.
    - You cannot enter letters when choosing a position.

![nameValidation](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/8a77f8a4-9dbe-4f02-919f-31410201b6f8)

![NumberValidation](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/9bfe52e0-7bc8-4540-b1f3-db3b9c0253e2)

![NumberValidation](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/0cb18672-16f3-461b-a054-bb14810c1163)

![NumberValidation](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/0006bc16-2eaa-4336-978f-5d2920188c2c)


## Design Features

### Game Title

    - For the title of the game I used ASCII art to generate an interesting and eye catching title. 

![title](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/d70b0e4f-b7b6-4b2d-80f6-512836640571)

### Text colors 

- __I used colorama to change the color of certain text within the game to enhance specific parts of the terminal and to make the game more eye catching.__

    - For Invalid input messages I used colorama to make the text red.
    - For the 'X' on the board to show the player positions I used colorama to make the text blue.
    - For the 'O' on the board to show the computer positons I used colorama to make the text lightMagenta.
    - I used colorama to make the winner message red and the looser message red. 

![errorMessage](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/9b38be5a-21f2-4f0c-9fa8-09f16b43a955)

![boardColors](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/6c89ed90-e2bf-4dbb-855e-92eb21c43e72)

![winnerMessage](https://github.com/Willr-hawkins/tic-tac-toe/assets/148203271/fee6f8ea-c739-4942-9262-bc5c86d2879b)