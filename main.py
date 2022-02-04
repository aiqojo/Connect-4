from Board import *
from random_ai import random_ai
from ai_handler import ai_handler
import game_handler

def main():

    width = 7
    height = 6
    sleep_time = 2

    board = Board(width, height)
    print(board)

    randy = ai_handler("random")

    game = game_handler(randy)

if __name__ == "__main__":
    main()