from Board import *
from ai_handler import ai_handler
from game_handler import game_handler
import time
import concurrent.futures

#randogenius
#randoprodigy

def main():
    run_cycle(1000000)



def run_cycle(rounds):

    total_start_time = time.time()
    epoch_total_time = 0
    epoch_count = 0

    red_wins = 0
    yellow_wins = 0
    ties = 0

    # Color can either be "X" for red, or "O" for yellow

    board = Board(False)
    # player        -> ai_handler("player", color, 0)
    # randy         -> ai_handler("randy", color, 0)
    # randosmart    -> ai_handler("randosmart", color, 0)
    # miniminimax   -> ai_handler("miniminimax", color, depth)
    
    
    red = ai_handler("miniminimax", "X", 10)
    yellow = ai_handler("randy", "O", 0)

    game = game_handler(board, red, yellow, 2, True)
    

    start_time = time.time() 

    for i in range(1, rounds + 1):

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
            epoch_count += 1
            epoch_time = time.time()
            print("ITERATION:", i, "VALUES:", red_wins, yellow_wins, ties)
            print("ABOVE EPOCH TOOK:", epoch_time - start_time, "SECONDS")
            epoch_total_time += (epoch_time - start_time)
            print("AVERAGE EPOCH TIME:", epoch_total_time/epoch_count)

            start_time = time.time()
                

    print("FINAL:", red_wins, yellow_wins, ties)

    total_end_time = time.time()

    print(total_end_time - total_start_time)

    return red_wins, yellow_wins, ties



if __name__ == "__main__":
    main()