from Board import *
from ai_handler import ai_handler
from game_handler import game_handler
import time
import concurrent.futures

#randogenius
#randoprodigy

def main():
    run_cycle(100000)



def run_cycle(rounds):

    total_start_time = time.time()

    red_wins = 0
    yellow_wins = 0
    ties = 0

    width = 7
    height = 6
    sleep_time = 2

    colors = ["X", "O"]

    board = Board(width, height, False)
    red = ai_handler("randosmart", colors, 0)
    yellow = ai_handler("randosmart", colors, 1)
    game = game_handler(board, red, yellow, 0.00, False)
    

    start_time = time.time() 

    for i in range(1, rounds):

        winner = game.play_round()

        # X means red wins, O means yellow wins
        if winner == "X":
            red_wins += 1
        elif winner == "O":
            yellow_wins += 1
        elif winner == "T":
            ties += 1

        #print("\n")

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