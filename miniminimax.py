import random
from time import sleep
from Board import Board
from copy import deepcopy
import numpy as np
from numpy import Inf

class miniminimax:

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth - 1
        if color == "X":
            self.opposite_color = "O"
        else:
            self.opposite_color = "X"
        self.print = True
    

    # Takes in a board
    # 
    # Takes in the array of empty columns on the board as well as the board
    def answer(self, arr, board):
        best_column = 0
        # The current best evaluation is set as -Inf so it can get overwritten by any other move
        best_val = -Inf
        # For each column in the board, start a recursive search for all 
        for column in board.find_empty_columns():
            board.add_piece(self.color, column)
            if self.print:
                print("LOOKING AT LOCATION", board.find_lowest(column), column)
                print(board)
            value = self.minimax(board, self.depth, self.color, column)
            remove = board.remove_piece(column)
            if not remove:
                print("REMOVE DIDN'T WORK")
            if value > best_val:
                best_val = value
                best_column = column
        
        # If the best eveluation was 0, there are no wins within the depth checked, so just pick random one
        if best_val == 0:
            if self.print:
                print("THERE WAS NO GOOD CHOICE PICKING RANDOM")
            return random.choice(arr)
        elif best_val == -Inf:
            return -1
        # Otherwise, there was a win, send that through
        else:
            if self.print:
                print("I SAW A WIN! IT STARTS AT COLUMN:", best_column)
            return best_column









    def minimax(self, board, depth, color, column):
        empty_columns = board.find_empty_columns()
        is_win = board.check_win_optimized(column)

        if self.print:
            sleep(.5)
            print("\n-------------------------")
            print("BOARD BELOW BEING CHECKED")
            print("DEPTH:", depth)
            print(board)
            print("COLUMN BEING CHECKED:", column)
            print("BOARD WIN?", is_win)

        # If there are no more columns, its a tie, return 0
        if len(empty_columns) == 0:
            if self.print:
                print("RETURNING 0, NO MORE COLUMNS")
            return 0

        # If the current color is this minimaxer's color, and there is a win, return 100 for win
        elif depth == 0 and color == self.color and is_win:
            if self.print:
                print("RETURNING 100, I WON")
            return 100

        # Else, the opponent won here, return -100
        elif depth == 0 and color == self.opposite_color and is_win:
            if self.print:
                print("RETURNING -100, I LOST")
            return -100

        # Otherwise, no information gained, report 0 back
        elif depth == 0:
            if self.print:
                print("RETURNING 0, THERE WAS NO WIN FOR EITHER")
            return 0

        # It only enteres here as long as depth isn't 0
        else:
            if color == self.color:
                bestVal = -Inf
                for new_column in empty_columns:
                    board.add_piece(self.color, column)
                    if self.print:
                        print("LOOKING AT LOCATION", board.find_lowest(column) + 1, column)
                        print(board)
                    value = self.minimax(board, depth-1, self.opposite_color, new_column)
                    remove = board.remove_piece(column)
                    if not remove:
                        print("REMOVE DIDN'T WORK")
                    bestVal = max(bestVal, value)
                return bestVal
            else:
                bestVal = Inf
                for new_column in empty_columns:
                    board.add_piece(self.opposite_color, column)
                    if self.print:
                        print("LOOKING AT LOCATION", board.find_lowest(column), column)
                        print(board)
                    value = self.minimax(board, depth-1, self.color, new_column)
                    remove = board.remove_piece(column)
                    if not remove:
                        print("REMOVE DIDN'T WORK")
                    bestVal = min(bestVal, value)
                return bestVal
