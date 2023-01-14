# Battleships

This is my interpretation of the popular board game, battleships. It allows the player to challenge themselves against the computer, which randomly generates ships depending on the grid size chosen by the player. The player will try guess where all of the ships are hidden and if they manage to find them they win the game.
This battleships game is simple and easy to use for players of all ages. The simplicity of the programme results in quick, fun games.

## Features

### Existing/current Features

* Opening Message

    * This message welcomes the player to the game.
    * Asks the player to enter which size of grid they'd like to play on (this is essentially choosing the difficulty of the game).

![opening message](/assets/images/welcome-message.png)

* Rules

    * This section first congratulates the player for entering the grid size.
    * The rules then are to seek out all of the enemy ships.
    * If the user manages to find them all they win the game 

![rules message](/assets/images/rules-message.png)

* Grid and Co-ordinate Inputs

    * The grid is printed depending on the size the player entered.
    * The number of ships that are on the grid are then stated. 
    * The player is then asked for the row which they'd like to target.
    * Then the column they'd like to target.

![grid and inputs](/assets/images/grid-and-inputs.png)

* Game Outcomes 

    * If the player guesses where one of the ships are correctly they are congratulated.
    * If the player guesses incorrectly they are given a message saying they have missed.
    * The player repeats the guessing process until either all ships are sunk or they have used all of their shots.
    * If the player manages to sink all of the ships they are again congratulated on winning the game.
    * If the player uses all of their shots they are told better luck next time.

### Potential Future Features

* Boards for computer and player
    * This would mean that the player and computer would go head to head in order to see who can sink the others ships.
* Ship Placement
    * This would go hand in hand with the first potential feature. If the player had a board they could pick where they'd like to place their ships allowing it to be more immersive.
* Refresh grid instead of continuously printing it
    * This would mean the programme would all be on one screen and save the need for any scrolling. It would also make the game look alot cleaner and more presentable.
* Play again button
    * I would have liked to have added a button which would refresh the game and let the user play again. I however, didn't have enough time to do so.

## Testing 

### PEP8

* I used the Code Institutes own PEP8 Python linter. This passed me 2 errors which are to do with the length of lines. However, when I try to fix by putting the code across 2 lines the code doesn't work.

### Browser Compatability

* The programme has been tested on the following browsers:
    * Chrome
    * Firefox
    * Safari

### Bugs 

#### Solved Bugs

* There was a problem initially in the "validate coordinates" function where if they player would guess the same co-ordinates it would still count it as though a shot had been taken. After going over the code I figured out that the problem was easily solved by adding a simple continue statement within the if statement that checks if the player has already guessed those co-ordinates.
* There was another problem I came across in the "validate coordinates" function where if the player would guess a letter that wasn't on the grid it would pass an error, stopping the game. I realised the problem was that I only had values for letters up to "H". I fixed this by assigning all letters a value from 1-26.

#### Unsolved Bugs

* There are no unsolved bugs that I am aware of.

## Deployment

This game was deployed through Heroku, using the Code Institutes mock terminal.

* Steps for deployment:
    * Fork/clone the repository
    * Create a new app on Heroku
    * Set the buildpacks to Python and NodeJS, in that order
    * Link the app on Heroku to the repository
    * Click on the "deploy" button


## Credits

Multiple resources where used in the making of this game.

* Austin Montgomery's [Python for Beginners: Battleship](https://bigmonty12.github.io/battleship).
* [This Trinket page](https://trinket.io/python/051179b6d3).
* [This rtodto page](https://rtodto.net/a-simple-battleship-python-script/).
* [Stackoverflow](https://stackoverflow.com/) helped with a lot of the questions or small issues I had.
* The Code Institutes slack community also deserves credit as there were multiple occasions when I turned to them for help.
