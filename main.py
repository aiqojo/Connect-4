from Board import *
from Zobrist import *
from ai_handler import ai_handler
from game_handler import game_handler
import time

#randogenius
#randoprodigy

def main():  
    run_cycle(1)

def run_cycle(rounds):

    epoch_total_time = 0
    epoch_count = 0

    red_wins = 0
    yellow_wins = 0
    ties = 0

    # Set true or false if you want extra stuff printed into terminal
    zobrist = Zobrist()
    board = Board(False)

    # player        -> ai_handler("player", color, 0)
    # randy         -> ai_handler("randy", color, 0)
    # randosmart    -> ai_handler("randosmart", color, 0)
    # miniminimax   -> ai_handler("miniminimax", color, depth)
    
    # Color can either be "X" for red, or "O" for yellow
    red = ai_handler("mediminimax", "X", 11)
    yellow = ai_handler("mediminimax", "O", 11)

    # The 4th parameter is time between rounds
    # Set from .25-2 seconds for ease of viewing, otherwise set to 0
    # Last parameter is for having it print into the terminal
    game = game_handler(board, zobrist, red, yellow, 0, True)
    
    total_start_time = time.time()
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
        #print(board)
        #print(board.__hash__())
        board.reset()
    
        if i % 1 == 0 and i != 0:
            epoch_count += 1
            epoch_time = time.time()
            print(red.name, "RED DEPTH:", red.ai.depth, yellow.name, "YELLOW DEPTH:", yellow.ai.depth)
            print("ITERATION:", i, "VALUES:", red_wins, yellow_wins, ties)
            print("ABOVE EPOCH TOOK:", epoch_time - start_time, "SECONDS")
            epoch_total_time += (epoch_time - start_time)
            print("AVERAGE EPOCH TIME:", epoch_total_time/epoch_count)
            print("-------------------")
            start_time = time.time()
            

    print("FINAL:", red_wins, yellow_wins, ties)
    total_end_time = time.time()
    print("TOTAL TIME:",total_end_time - total_start_time)


    print("ap:", board.add_piece_count, "\nrp:", board.remove_piece_count, "\nfe:", \
        board.find_empty_columns_count, "\ncw:", board.check_win_optimized_count)
    print("red minimax calls:", red.ai.minimax_count)
    print("yellow minimax calls:", yellow.ai.minimax_count)

    return red_wins, yellow_wins, ties

if __name__ == "__main__":
    main()