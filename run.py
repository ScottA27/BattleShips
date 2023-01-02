from random import randint

board = []

while True:
    board_size = input("Enter board size: ")
    if board_size.isdigit():
        board_size = int(board_size)
        if board_size >= 3 and board_size <= 10:
            print("Well done now let's get this game started!")
            break
        else:
            print("You must enter a number between 3 and 10 in order to play!")
    else:
        print("You must enter a number between 3 and 10 in order to play!")
        continue


def build_board():
    """
    Gets the size of the board and builds it
    """
    for x in range(board_size):
        board.append(["O"] * board_size)
    return board_size


def print_board():
    """
    Prints the board
    """
    for row in board:
        print((" ").join(row))


build_board()
print_board()

