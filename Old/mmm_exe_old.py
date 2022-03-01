from copy import copy
import random
from time import sleep
from Board import Board
import numpy as np
import concurrent.futures
from numpy import Inf

class miniminimax:

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth

        if color == "X":
            self.opposite_color = "O"
        else:
            self.opposite_color = "X"

        self.print = False
        self.delay = 0

        self.answer_count = 0
        self.minimax_count = 0

    # Method to return the final answer of the minimax
    # Takes in arr of empty columns for random choice at end
    # Takes in board which it will directly manipulate as it searches for answer
    def answer(self, arr, board, zobrist):
        print("COLUMNS", arr)
        print(zobrist.count)
        zobrist.clear()
        self.answer_count += 1
        
        # These lists will hold the most optimal next moves and return a random one at the end
        next_turn_win_choices = []

        # Just looking if there is a win next turn so I can quickly return before
        # going into the minimax 
        for column in arr:
            board.add_piece(self.color, column, zobrist)
            is_win = board.check_win_optimized(column)
            board.remove_piece(column, zobrist)

            if is_win:
                if self.print:
                    print("I HAVE AN ANSWER:", column)
                next_turn_win_choices.append(column)

        if next_turn_win_choices:
            return random.choice(next_turn_win_choices)

        # ------------------------
        # ------Multiprocess------
        # ------------------------

        value_list = []
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for i in arr:
                process_values = executor.submit(self.minimax_process_helper, zobrist, board, \
                                                self.depth, self.color, i)
                print("done with",i)
                value_list.append(process_values.result())

        max_value = max(value_list)
        choices = [index for index, value in enumerate(value_list) if value == max_value]
        print("VALUE_LIST", value_list)
        print("CHOICES", choices)
        #print("ZOBRIST",self.hash_table_count_total)
        choice = random.choice(choices)
        print("CHOICE", choice)
        return arr[choice]


    def minimax_process_helper(self, zobrist, board, depth, color, column):
        temp_board = copy(board)
        temp_board.add_piece(color, column, zobrist)
        ans = self.minimax(zobrist, temp_board, depth, self.opposite_color)
        temp_board.remove_piece(column, zobrist)
        return ans


    def minimax(self, zobrist, board, depth, color):
        cur_hash = zobrist.zHash
        if cur_hash in zobrist.board_table:
            print("ENETERED", zobrist.count)
            zobrist.count += 1
            print(zobrist.count)
            return zobrist.board_table[cur_hash]

        self.minimax_count += 1
        if self.print:
            sleep(self.delay)

        DEFAULT_SCORE = 0

        # If at 0 depth and here, no information was gained, return default score
        if depth == 0:
            if self.print:
                print("NO INFO GAINED, RETURN 0")
            zobrist.board_table[cur_hash] = DEFAULT_SCORE
            return DEFAULT_SCORE
        
        # Or if there are no more empty columns, return default score, it's a tie
        empty_columns = board.find_empty_columns()
        #print(empty_columns)
        if not empty_columns:
            if self.print:
                print("NO MORE COLUMNS LEFT, RETURN 0")
            zobrist.board_table[cur_hash] = DEFAULT_SCORE
            return DEFAULT_SCORE
        
        if color == self.color:
            best_score = -Inf
        else:
            best_score = Inf

        WIN_SCORE = 100 * depth
        LOSE_SCORE = -100 * depth

        for column in empty_columns:
            board.add_piece(color, column, zobrist)
            is_win = board.check_win_optimized(column)

            if self.print:
                print(board)

            if is_win:
                board.remove_piece(column, zobrist)
                if color == self.color:
                    if self.print:
                        print("I WON, RETURN 100", depth)
                    zobrist.board_table[cur_hash] = WIN_SCORE
                    return WIN_SCORE
                else:
                    if self.print:
                        print("I LOST RETURN -100", depth)
                    zobrist.board_table[cur_hash] = LOSE_SCORE
                    return LOSE_SCORE

            if color == self.color:
                score = self.minimax(zobrist, board, depth - 1, self.opposite_color)
            else:
                score = self.minimax(zobrist, board, depth - 1, self.color)

            if color == self.color:
                if score > best_score:
                    best_score = score
            else:
                if score < best_score:
                    best_score = score

            board.remove_piece(column, zobrist)

        # For loop for each legal move
            # Add the piece
            # Check win
            # If it wins, return the score dependent on wether color is self.color or self.opposite_color
            # SCORE = Otherwise, call next depth with this board
            # Remove the move
        return best_score




    