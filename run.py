from random import randint

grid = []
NUM_OF_SHIPS = 10
all_ship_locations = []
SHIPS_HIT = 0

print("---------------------------------------------")
print("           Welcome To Battleships            ")
print("First, lets pick the size of the grid you")
print("would like to play on. Just enter a number")
print("between 3 and 8. 3 is the easiest and if you")
print("want a real test 8 is the most difficult.")
print("---------------------------------------------")
# While statement asks user which grid size they'd like to play with
while True:
    GRID_SIZE = input("Please enter the grid size here:\n")
    if GRID_SIZE.isdigit():
        GRID_SIZE = int(GRID_SIZE)
        if GRID_SIZE >= 3 and GRID_SIZE <= 8:
            print("---------------------------------------------")
            print("Well done now let's get this game started!")
            break
        else:
            print("You must enter a number between 3 and 8 in order to play!")
    else:
        print("You must enter a number between 3 and 8 in order to play!")
        continue


print("---------------------------------------------")
print("Now you'll pick co-ordinates to seek out the")
print("enemy ships. If you manage to sink all the")
print("ships on the field you win the game!")


def build_grid():
    """
    Gets the size of the board and builds the rows
    """
    for x in range(GRID_SIZE):
        grid.append(["O"] * GRID_SIZE)
    return GRID_SIZE


def print_grid():
    """
    Builds the entire grid and prints it
    """
    print("---------------------------------------------")
    column_names = "ABCDEFGH"[:GRID_SIZE]
    print('  ' + ' '.join(column_names))
    row_number = 1
    for row in grid:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print("---------------------------------------------")


def build_ships():
    """
    Building and placing the ships on the board
    """
    global NUM_OF_SHIPS
    placed_ships = 0
    if GRID_SIZE >= 3 and GRID_SIZE <= 4:
        NUM_OF_SHIPS = 3
        while placed_ships != NUM_OF_SHIPS:
            ship_row = randint(1, (GRID_SIZE))
            ship_column = randint(1, (GRID_SIZE))
            ship_position = [ship_row, ship_column]
            all_ship_locations.append(ship_position)
            placed_ships += 1
    elif GRID_SIZE >= 5 and GRID_SIZE <= 6:
        NUM_OF_SHIPS = 5
        while placed_ships != NUM_OF_SHIPS:
            ship_row = randint(1, (GRID_SIZE))
            ship_column = randint(1, (GRID_SIZE))
            ship_position = [ship_row, ship_column]
            all_ship_locations.append(ship_position)
            placed_ships += 1
    else:
        NUM_OF_SHIPS = 10
        while placed_ships != NUM_OF_SHIPS:
            ship_row = randint(1, (GRID_SIZE))
            ship_column = randint(1, (GRID_SIZE))
            ship_position = [ship_row, ship_column]
            all_ship_locations.append(ship_position)
            placed_ships += 1


def validate_coordinates():
    """
    Takes cooridinates from the player and checks if they are valid.
    If valid this will use the given coordinates to see if the player
    has hit or missed a ship.
    This will also print win/loss message at the end of the game.
    """
    global SHIPS_HIT
    letters_to_numbers = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
        "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
        "Z": 26
        }

    row_list = [x + 1 for x in list(range(GRID_SIZE))]

    print(f"You have hit {SHIPS_HIT} ships out of {NUM_OF_SHIPS}!")

    tries = (GRID_SIZE * GRID_SIZE) // 2
    while tries > 0:
        guess_row = input("Please choose the row you'd like to hit:\n")
        if guess_row.isdigit():
            guess_row = int(guess_row)
            if guess_row not in row_list:
                print("Out of bounds, you must pick a row within the grid!")
                continue
        else:
            print("You must enter a number within the grid!")
            continue
        while True:
            guess_column = input(
                "Please choose the column you'd like to hit:\n").upper()
            if guess_column.isalpha():
                guess_column = letters_to_numbers[guess_column]
                if guess_column not in row_list:
                    print(
                        "Out of bounds, you must pick a column within the grid!")
                    continue
                else:
                    break
            else:
                print("You must enter a letter within the grid!")
                continue
        guess = [guess_row, guess_column]
        if grid[guess_row - 1][guess_column - 1] == "X" or grid[guess_row - 1][guess_column - 1] == "-":
            print("---------------------------------------------")
            print("You've already guessed that one!")
            continue
        if guess in all_ship_locations:
            print("---------------------------------------------")
            print("You sunk a ship!")
            grid[guess_row - 1][guess_column - 1] = "X"
            SHIPS_HIT += 1
        else:
            print("---------------------------------------------")
            print("You failed to hit a target!")
            grid[guess_row - 1][guess_column - 1] = "-"
        if SHIPS_HIT == NUM_OF_SHIPS:
            print_grid()
            print("Contgratulations you have won battleships!")
            print("---------------------------------------------")
            break
        else:
            tries -= 1
            print(f"You have hit {SHIPS_HIT} ships out of {NUM_OF_SHIPS}!")
            print(f"You have {tries} shots left.")
            if tries == 0:
                print_grid()
                print("You have lost, better luck next time!")
                print("---------------------------------------------")
                break
        print_grid()


def run_game():
    """
    Run Game function.
    Takes all of the above functions and puts them in the correct order.
    """
    build_grid()
    print_grid()
    build_ships()
    validate_coordinates()


run_game()
