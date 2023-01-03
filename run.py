from random import randint

grid = []
num_of_ships = 8
all_ship_locations = []


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


letters = "ABCDEFGHIJ"


def print_grid():
    """
    Builds the entire grid and prints it
    """
    column_letters = letters[0: (grid_size)]
    print(" %s%s" % (" ", " ".join(column_letters)))
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
    

build_grid()
print_grid()
build_ships()
