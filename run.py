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
    Gets the size of the board and builds the rows
    """
    for x in range(board_size):
        board.append(["O"] * board_size)
    return board_size


letters = "ABCDEFGHIJ"


def print_board():
    """
    Builds the entire board and prints it
    """
    column_letters = letters[0: (board_size)]
    print(" %s%s" % (" ", " ".join(column_letters)))
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


build_board()
print_board()

def random_row():
    return randint(1,len(board))


def random_column():
    return randint(1,len(board[0]))


print(random_row())
print(random_column())