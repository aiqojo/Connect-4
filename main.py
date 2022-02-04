from Board import *
from random_ai import random_ai
from ai_handler import ai_handler
from game_handler import game_handler

def main():

    width = 7
    height = 6
    sleep_time = 2

    board = Board(width, height)
    print(board)

    randy = ai_handler("random")

    game = game_handler(board, randy, randy, 1)

    winner = game.play_round()




if __name__ == "__main__":
    main()