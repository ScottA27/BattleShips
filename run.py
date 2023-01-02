from random import randint

# global variables
board_size = None


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