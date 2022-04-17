from copy import copy
from functools import partial
import random
from time import sleep
from Board import Board
import numpy as np
import multiprocessing as mp
from numpy import Inf

class mediminimax:

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
        if self.print:
            print("COLUMNS", arr)
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
                next_turn_win_choices.append(column)

        if next_turn_win_choices:
            if self.print:
                print("Zobrist matches", zobrist.count)
            zobrist.clear()
            choice = random.choice(next_turn_win_choices)
            if self.print:
                print("CHOICE", choice)
            return choice


        # If it gets here there is no next turn win so we start the minimax for each column
        value_list = []

        #arr = self.optimized_order(board, arr)
        if self.print:
            print("Optimized order:", arr)

        for column in arr:
            board.add_piece(self.color, column, zobrist)
            value = self.minimax(zobrist, board, self.depth, -Inf, Inf, self.opposite_color)
            board.remove_piece(column, zobrist)
            value_list.append(value)

        # This is graabing the list of largest value or values if tied
        max_value = max(value_list)
        choices = [index for index, value in enumerate(value_list) if value == max_value]

        if self.print:
            print("VALUE_LIST", value_list)
            print("CHOICES", choices)
        
        # This picks a random choice from the choices list then finds the column of that choice in the original array
        choice = random.choice(choices)
        if self.print:
            print("Zobrist matches", zobrist.count)
            zobrist.clear()
            print("CHOICE", choice)
        return arr[choice]

    # This method should help speed up the minimax function
    # It does that by ordering the columns in an optimized way
    # If the minimax function is able to find a higher score for a specific choice from the beginning
    # it can prune more branches as it continues and take less time to give a result
    def optimized_order(self, board, arr):
        opt_arr = []

        for i in range(6):
            if board.last_column + i <= 6 and board.last_column + i not in opt_arr and board.last_column + i in arr:
                opt_arr.append(board.last_column + i)
            if board.last_column - i >= 0  and board.last_column - i not in opt_arr  and board.last_column - i in arr:
                opt_arr.append(board.last_column - i)

        if len(opt_arr) == 0:
            return arr

        return opt_arr

    # Alpha is red's best evaluation, beta is yellow's
    def minimax(self, zobrist, board, depth, alpha, beta, color):
        self.minimax_count += 1
        if self.print:
            sleep(self.delay)

        cur_hash = zobrist.zHash
        if cur_hash in zobrist.board_table:
            #print("ENETERED", zobrist.count)
            zobrist.count += 1
            #print(zobrist.count)
            return zobrist.board_table[cur_hash]

        DEFAULT_SCORE = 0

        # If at 0 depth and here, no information was gained, return default score
        if depth == 0:
            zobrist.board_table[cur_hash] = DEFAULT_SCORE
            return DEFAULT_SCORE
        
        # Or if there are no more empty columns, return default score, it's a tie
        empty_columns = board.find_empty_columns()
        #print(empty_columns)
        if not empty_columns:
            zobrist.board_table[cur_hash] = DEFAULT_SCORE
            return DEFAULT_SCORE
        
        WIN_SCORE = 100 * depth
        LOSE_SCORE = -100 * depth

        if color == self.color:
            max_score = -Inf

            for column in empty_columns:
                board.add_piece(color, column, zobrist)
                is_win = board.check_win_optimized(column)
                
                # If the self.color wins here, return win score
                if is_win:
                    board.remove_piece(column, zobrist)
                    zobrist.board_table[cur_hash] = WIN_SCORE
                    return WIN_SCORE
                
                # Otherwise, it hasn't won yet and there are still depths to be traversed
                eval = self.minimax(zobrist, board, depth - 1, alpha, beta, self.opposite_color)
                board.remove_piece(column, zobrist)
                # Checking if the minimax found a better choice (for maximizing player)
                max_score = max(max_score, eval)
                # Setting alpha equal to the max score to show the best choice self.color can take
                alpha = max(alpha, eval)
                # If beta is less than alpha, that means self.opposite_color had a better move previously
                # and there is no reason to continue down this tree
                if beta <= alpha:
                    break
            return max_score

        # If opposite color, enter here
        else:
            min_score = Inf

            for column in empty_columns:
                board.add_piece(color, column, zobrist)
                is_win = board.check_win_optimized(column)

                if is_win:
                    board.remove_piece(column, zobrist)
                    zobrist.board_table[cur_hash] = LOSE_SCORE
                    return LOSE_SCORE
                
                # Otherwise, it hasn't won yet and there are still depths to be traversed
                eval = self.minimax(zobrist, board, depth - 1, alpha, beta, self.color)
                board.remove_piece(column, zobrist)
                # Checking if the minimax found a better choice (for minimizing player)
                min_score = min(min_score, eval)
                # Setting beta equal to the min score to show the best choice self.opposite_color can take
                beta = min(beta, eval)
                # If beta is less than alpha, that means self.color had a better move previously
                # and there is no reason to continue down this tree
                if beta <= alpha:
                    break
            return min_score
            