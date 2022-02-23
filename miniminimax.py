import random
from time import sleep

from numpy import Inf

class miniminimax:

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth - 1

        if color == "X":
            self.opposite_color = "O"
        else:
            self.opposite_color = "X"

    def answer(self, arr, board):
        best_column = 0
        best_val = -Inf
        for column in board.find_empty_columns():
            temp_board = board
            temp_board.add_piece(self.color,column)
            value = self.minimax(temp_board, self.depth, self.opposite_color)
            if value > best_val:
                best_val = value
                best_column = column
        
        return best_column


    def minimax(self, board, depth, color):
        sleep(1)
        print("DEPTH:", depth)
        print(board)
        if depth == 0:
            return 0
        elif len(board.find_empty_columns()) == 0:
            return 0
        elif depth == 0 and color == self.color and board.check_win_optimized():
            for column in board.find_empty_columns():
                temp_board = board
                if temp_board.check_win_optimized(column):
                    return 100
        elif depth == 0 and color == self.opposite_color and board.check_win_optimized():
            for column in board.find_empty_columns():
                temp_board = board
                if temp_board.check_win_optimized(column):
                    return -100
        else:
            if color == self.color:
                bestVal = -Inf
                for column in board.find_empty_columns():
                    temp_board = board
                    temp_board.add_piece(self.color,column)
                    value = self.minimax(temp_board, depth-1, self.opposite_color)
                    bestVal = max(bestVal, value)
                    return bestVal
            else:
                bestVal = Inf
                for column in board.find_empty_columns():
                    temp_board = board
                    temp_board.add_piece(self.opposite_color,column)
                    value = self.minimax(temp_board, depth-1, self.color)
                    bestVal = min(bestVal, value)
                    return bestVal
        return bestVal

