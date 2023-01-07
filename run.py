from random import randint

grid = []
num_of_ships = 10
all_ship_locations = []

ALPHABET =['A', 'B', 'C', 'D', 'E', 'F', 'G']


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
    column_names = ALPHABET[:grid_size]
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
    try:
        guess_row = input("Please choose the row you'd like to hit: ")
        while guess_row not in grid_size:
            print("Out of bounds, you must pick a row within the grid!")
            guess_row

        guess_column = input("Please choose the column you'd like to hit: ").upper()
        while guess_column not in column_names:
            print("Out of bounds, you must pick a column within the grid!")
            guess_column.upper()
        
        return int(guess_row), ALPHABET.index(guess_column)


build_grid()
print_grid()
build_ships()
validate_coordinates()
