from Board import *
from ai_handler import ai_handler
from game_handler import game_handler
import time

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

    # Set true or false if you want extra stuff printed into terminal
    board = Board(False)
    #print(board)

    # player        -> ai_handler("player", color, 0)
    # randy         -> ai_handler("randy", color, 0)
    # randosmart    -> ai_handler("randosmart", color, 0)
    # miniminimax   -> ai_handler("miniminimax", color, depth)
    
    # Color can either be "X" for red, or "O" for yellow
    red = ai_handler("miniminimax", "X", 3)
    yellow = ai_handler("miniminimax", "O", 3)

    # The 4th parameter is time between rounds
    # Set from .25-2 seconds for ease of viewing, otherwise set to 0
    # Last parameter is for having it print into the terminal
    game = game_handler(board, red, yellow, 0, False)
    
    start_time = time.time() 

    for i in range(1, rounds + 1):

        winner = game.play_round()
        # X means red wins, O means yellow wins, T is tie
        if winner == "X":
            red_wins += 1
        elif winner == "O":
            yellow_wins += 1
        elif winner == "T":
            ties += 1

        # If I wanted to, I could also decide to save stuff to a file here in future
        board.reset()
    
        if i % 10 == 0 and i != 0:
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