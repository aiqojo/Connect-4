from Board import *
from random_ai import random_ai
from ai_handler import ai_handler
from game_handler import game_handler

def main():

    width = 7
    height = 6
    sleep_time = 2

    board = Board(width, height, False)
    print(board)

    randy = ai_handler("random")

    # game = game_handler(board, randy, randy, 2)

    # winner = game.play_round()

    red_wins = 0
    yellow_wins = 0
    ties = 0

    for i in range(1000):
        game = game_handler(board, randy, randy, 0, False)
        winner = game.play_round()

        # X means red wins, O means yellow wins
        if winner == "X":
            red_wins += 1
        elif winner == "O":
            yellow_wins += 1
        elif winner == "T":
            ties += 1

        board.reset()

    print(red_wins, yellow_wins, ties)





if __name__ == "__main__":
    main()