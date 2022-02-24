import random
from time import sleep
from Board import Board
from copy import deepcopy

from numpy import Inf

class miniminimax:

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth
        if color == "X":
            self.opposite_color = "O"
        else:
            self.opposite_color = "X"
        self.print = True

    # Takes in an array of empty columns on the boardm as well as the board
    def answer(self, arr, board):
        best_column = 0
        best_val = -Inf
        # For each column in the board, start a recursive search for all 
        for column in board.find_empty_columns():
            temp_board = deepcopy(board)
            value = self.minimax(temp_board, self.depth, self.color, column)
            if value > best_val:
                best_val = value
                best_column = column
        
        # If the best eveluation was 0, there are no wins within the depth checked, so just pick random one
        if best_val == 0:
            if self.print:
                print("THERE WAS NO GOOD CHOICE PICKING RANDOM")
            return random.choice(arr)
        # Otherwise, there was a win, send that through
        else:
            if self.print:
                print("I SAW A WIN! IT STARTS AT COLUMN: ", best_column)
            return best_column


    def minimax(self, board, depth, color, column):
        if self.print:
            sleep(.005)
            print("\n-------------------------")
            print("BOARD BELOW BEING CHECKED")
            print("DEPTH:", depth)
            tb = deepcopy(board)
            tb.add_piece(color, column)
            print(tb)
            print("COLUMN BEING CHECKED:", column)
            print("BOARD WIN?", board.check_win_optimized(column))
        # If there are no more columns, its a tie, return 0
        if len(board.find_empty_columns()) == 0:
            if self.print:
                print("RETURNING 0, NO MORE COLUMNS")
            return 0
        # If the current color is this minimaxer's color, and there is a win, return 100 for win
        elif depth == 0 and color == self.color and board.check_win_optimized(column):
            if self.print:
                print("RETURNING 100, I WON")
            return 100
        # Else, the opponent won here, return -100
        elif depth == 0 and color == self.opposite_color and board.check_win_optimized(column):
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
                for new_column in board.find_empty_columns():
                    temp_board = deepcopy(board)
                    temp_board.add_piece(self.color,column)
                    if self.print:
                        print("LOOKING AT LOCATION", temp_board.find_lowest(column), column)
                    value = self.minimax(temp_board, depth-1, self.opposite_color, new_column)
                    bestVal = max(bestVal, value)
                return bestVal
            else:
                bestVal = Inf
                for new_column in board.find_empty_columns():
                    temp_board = deepcopy(board)
                    temp_board.add_piece(self.opposite_color,column)
                    if self.print:
                        print("NEWCOLUMN:",new_column)
                    value = self.minimax(temp_board, depth-1, self.color, new_column)
                    bestVal = min(bestVal, value)
                return bestVal
