import random
from time import sleep
from Board import Board
import numpy as np

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
        self.delay = .01
        self.answer_count = 0
        self.minimax_count = 0
        self.hash_table_count = 0
        self.board_table = {}

    # Method to return the final answer of the minimax
    # Takes in arr of empty columns for random choice at end
    # Takes in board which it will directly manipulate as it searches for answer
    def answer(self, arr, board):
        self.board_table.clear()

        self.answer_count += 1
        # These lists will hold the most optimal next moves and return a random one at the end
        next_turn_win_choices = []
        choices = []

        # The current best evaluation is set as -Inf so it can get overwritten by any other move
        choices_values = -Inf

        # Now, send the board and its current state into the minimax function
        for column in arr:
            board.add_piece(self.color, column)
            is_win = board.check_win_optimized(column)
            
            if is_win:
                board.remove_piece(column)
                if self.print:
                    print("I HAVE AN ANSWER:", column)
                next_turn_win_choices.append(column)
                continue
            
            value = self.minimax(board, self.depth, self.opposite_color)
            board.remove_piece(column)

            if value > choices_values:
                choices.clear()
                choices_values = value
                choices.append(column)
            elif value == choices_values:
                choices.append(column)

        print("HASH TABLE COUNT:", self.hash_table_count)

        if next_turn_win_choices:
            return random.choice(next_turn_win_choices)
        elif choices:
            return random.choice(choices)


    def minimax(self, board, depth, color):
        cur_hash = board.zHash
        if cur_hash in self.board_table:
            self.hash_table_count += 1
            return self.board_table[cur_hash]

        self.minimax_count += 1
        if self.print:
            sleep(self.delay)

        DEFAULT_SCORE = 0

        # If at 0 depth and here, no information was gained, return default score
        if depth == 0:
            if self.print:
                print("NO INFO GAINED, RETURN 0")
            self.board_table[cur_hash] = DEFAULT_SCORE
            return DEFAULT_SCORE
        
        # Or if there are no more empty columns, return default score, it's a tie
        empty_columns = board.find_empty_columns()
        #print(empty_columns)
        if not empty_columns:
            if self.print:
                print("NO MORE COLUMNS LEFT, RETURN 0")
            self.board_table[cur_hash] = DEFAULT_SCORE
            return DEFAULT_SCORE
        
        if color == self.color:
            best_score = -Inf
        else:
            best_score = Inf

        WIN_SCORE = 100 * depth
        LOSE_SCORE = -100 * depth

        for column in empty_columns:
            board.add_piece(color, column)
            is_win = board.check_win_optimized(column)

            if self.print:
                print(board)

            if is_win:
                board.remove_piece(column)
                if color == self.color:
                    if self.print:
                        print("I WON, RETURN 100", depth)
                    self.board_table[cur_hash] = WIN_SCORE
                    return WIN_SCORE
                else:
                    if self.print:
                        print("I LOST RETURN -100", depth)
                    self.board_table[cur_hash] = LOSE_SCORE
                    return LOSE_SCORE

            if color == self.color:
                score = self.minimax(board, depth - 1, self.opposite_color)
            else:
                score = self.minimax(board, depth - 1, self.color)

            if color == self.color:
                if score > best_score:
                    best_score = score
            else:
                if score < best_score:
                    best_score = score

            board.remove_piece(column)

        # For loop for each legal move
            # Add the piece
            # Check win
            # If it wins, return the score dependent on wether color is self.color or self.opposite_color
            # SCORE = Otherwise, call next depth with this board
            # Remove the move
        return best_score




    