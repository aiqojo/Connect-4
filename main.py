from Board import *
from random_ai import random_ai
from ai_handler import ai_handler
from time import sleep

def main():

    width = 7
    height = 6

    board = Board(width, height)
    print(board)

    randy = ai_handler("random")

    while True:
        value = -1

        print("Red's turn!")
        #value = input("Enter column: ")
        value = randy.answer(width)
        board.add_checker("r", value)
        print(board)

        if board.check_win():
            break

        sleep(.75)

        print("Yellow's turn!")
        #value = input("Enter column: ")
        value = randy.answer(width)
        board.add_checker("y", value)
        print(board)

        if board.check_win():
            break


if __name__ == "__main__":
    main()