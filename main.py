from Board import *
from ai_handler import ai_handler
from game_handler import game_handler
import time
import concurrent.futures

def main():
    run_cycle(1000000)






def run_cycle(rounds):

    total_start_time = time.time()

    red_wins = 0
    yellow_wins = 0
    ties = 0

    width = 7
    height = 6
    sleep_time = 2

    board = Board(width, height, False)
    red = ai_handler("player", "X")
    yellow = ai_handler("randosmart", "O")
    game = game_handler(board, red, yellow, 1, True)
    

    start_time = time.time() 

    for i in range(1, rounds):

        print(board)

        winner = game.play_round()

        # X means red wins, O means yellow wins
        if winner == "X":
            red_wins += 1
        elif winner == "O":
            yellow_wins += 1
        elif winner == "T":
            ties += 1

        print("\n")

        board.reset()
    
        if i % 1000 == 0 and i != 0:
                epoch_time = time.time()
                print("ITERATION:", i, "VALUES:", red_wins, yellow_wins, ties)
                print("ABOVE EPOCH TOOK:", epoch_time - start_time, "SECONDS")
                start_time = time.time()

    print("FINAL:", red_wins, yellow_wins, ties)

    total_end_time = time.time()

    print(total_end_time - total_start_time)

    return red_wins, yellow_wins, ties



if __name__ == "__main__":
    main()