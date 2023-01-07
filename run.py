from random import randint

grid = []
NUM_OF_SHIPS = 10
all_ship_locations = []
SHIPS_HIT = 0

while True:
    GRID_SIZE = input("Enter grid size: ")
    if GRID_SIZE.isdigit():
        GRID_SIZE = int(GRID_SIZE)
        if GRID_SIZE >= 3 and GRID_SIZE <= 8:
            print("Well done now let's get this game started!")
            break
        else:
            print("You must enter a number between 3 and 8 in order to play!")
    else:
        print("You must enter a number between 3 and 8 in order to play!")
        continue


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
    column_names = "ABCDEFGH"[:GRID_SIZE]
    print('  ' + ' '.join(column_names))
    row_number = 1
    for row in grid:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


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
    print(all_ship_locations)


def validate_coordinates():
    """
    Takes cooridinates from the player and checks if they are valid
    """
    global SHIPS_HIT
    letters_to_numbers = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8
        }

    row_list = [x + 1 for x in list(range(GRID_SIZE))]

    tries = (GRID_SIZE * GRID_SIZE) // 2
    while tries > 0:
        guess_row = input("Please choose the row you'd like to hit: ")
        guess_row = int(guess_row)
        while guess_row not in row_list:
            print("Out of bounds, you must pick a row within the grid!")
            guess_row = input("Please choose the row you'd like to hit: ")
            guess_row = int(guess_row)
        guess_column = input(
            "Please choose the column you'd like to hit: ").upper()
        guess_column = letters_to_numbers[guess_column]
        while guess_column not in row_list:
            print("Out of bounds, you must pick a column within the grid!")
            guess_column = input(
                "Please choose the column you'd like to hit: ").upper()
            guess_column = letters_to_numbers[guess_column]
        guess = [guess_row, guess_column]
        if guess in all_ship_locations:
            print("You sunk a ship!")
            grid[guess_row - 1][guess_column - 1] = "X"
            SHIPS_HIT += 1
        elif (grid[guess_row - 1][guess_column - 1]) == "X":
            print("You've already guessed that one!")
        elif (grid[guess_row - 1][guess_column - 1]) == "-":
            print("You've already guessed that one!")
        else:
            print("You failed to hit a target!")
            grid[guess_row - 1][guess_column - 1] = "-"
        if SHIPS_HIT == NUM_OF_SHIPS:
            print_grid()
            print("Contgratulations you have won!")
            break
        else:
            tries -= 1
            print(f"You have {tries} shots left.")
            if tries == 0:
                print_grid()
                print("You have lost, better luck next time!")
                break
        print_grid()


def run_game():
    build_grid()
    print_grid()
    build_ships()
    validate_coordinates()


run_game()