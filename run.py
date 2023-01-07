from random import randint

grid = []
num_of_ships = 10
all_ship_locations = []

letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

while True:
    grid_size = input("Enter grid size: ")
    if grid_size.isdigit():
        grid_size = int(grid_size)
        if grid_size >= 3 and grid_size <= 8:
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
    for x in range(grid_size):
        grid.append(["O"] * grid_size)
    return grid_size


def print_grid():
    """
    Builds the entire grid and prints it
    """
    column_names = "ABCDEFGH"[:grid_size]
    print('  ' + ' '.join(column_names))
    row_number = 1
    for row in grid:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def build_ships():
    """
    Building and placing the ships on the board
    """
    placed_ships = 0
    if grid_size >= 3 and grid_size <= 4:
        num_of_ships = 3
        while placed_ships != num_of_ships:
            ship_row = randint(1, (grid_size))
            ship_column = randint(1, (grid_size))
            ship_position = [ship_row, ship_column]
            all_ship_locations.append(ship_position) 
            placed_ships += 1
    elif grid_size >= 5 and grid_size <= 6:
        num_of_ships = 5
        while placed_ships != num_of_ships:
            ship_row = randint(1, (grid_size))
            ship_column = randint(1, (grid_size))
            ship_position = [ship_row, ship_column]
            all_ship_locations.append(ship_position) 
            placed_ships += 1
    else:
        num_of_ships = 10
        while placed_ships != num_of_ships:
            ship_row = randint(1, (grid_size))
            ship_column = randint(1, (grid_size))
            ship_position = [ship_row, ship_column]
            all_ship_locations.append(ship_position) 
            placed_ships += 1
    print(all_ship_locations)


def validate_coordinates():
    """
    Takes cooridinates from the player and checks if they are valid
    """
    guess_row = input("Please choose the row you'd like to hit: ")
    guess_row = int(guess_row)
    while guess_row not in list(range(grid_size)):
        print("Out of bounds, you must pick a row within the grid!")
        guess_row = input("Please choose the row you'd like to hit: ")

    guess_column = input(
        "Please choose the column you'd like to hit: ").upper()
    guess_column = letters_to_numbers[guess_column]
    while guess_column not in list(range(grid_size)):
        print("Out of bounds, you must pick a column within the grid!")
        print(guess_column)
        guess_column = input(
            "Please choose the column you'd like to hit: ").upper()
    guess = [guess_row, guess_column]
    if guess in all_ship_locations:
        print("You sunk a ship!")
        grid[guess_row - 1][guess_column - 1] = "X"
    elif (grid[guess_row - 1][guess_column - 1]) == "X":
        print("You've already guessed that one!")
    elif (grid[guess_row - 1][guess_column - 1]) == "-":
        print("You've already guessed that one!")
    else:
        print("You failed to hit a target!")
        grid[guess_row - 1][guess_column - 1] = "-"


build_grid()
print_grid()
build_ships()
validate_coordinates()