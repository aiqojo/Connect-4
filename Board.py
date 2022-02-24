#board[row][column]
import numpy as np

class Board(object):

    p1 = "X"
    p2 = "O"

    def __init__(self, print):
        self.WIDTH = 7
        self.HEIGHT = 6
        self.print = print

        self.board = np.empty((6,7), dtype='str')
        self.board[:] = ' '
        self.board_history = ''


    def reset(self):
        if self.print:
            print("-------NEW GAME-------")
        self.board = np.zeros((6,7), dtype='str')
        self.board[:] = ' '
        self.board_history = ''

    def get_board_state(self):
        return self.board_history


    def add_piece(self, color, column):
        column = int(column)
        row = self.find_lowest(column)
        if row == -1:
            return False
        else:
            # if self.print:
            #     print("COLOR:", color, "ROW:", row, "COLUMN:", column)
            self.board_history += str(column)
            self.board[row,column] = color.upper()
            return True

    def remove_piece(self,column):
        row = self.find_lowest(column) + 1
        if row >= 6:
            return False
        else:
            # if self.print:
            #     print("COLOR:", self.board[row,column], "ROW:", row, "COLUMN:", column)
            self.board[row,column] = ' '
            return True

    def find_empty_columns(self):
        arr = list(range(0, self.WIDTH))
        arrr = []

        for x in arr:
            if not self.find_lowest(x) == -1:
                arrr.append(x)
        #print("Column choices:", arrr)
        return arrr


    def get_location_color(self, row, column):
        return self.board[row,column]


    # Find lowest
    # If lowest isn't found, return -1, as nothing can be placed in that row
    def find_lowest(self, column):
        lowest = -1

        for x in reversed(range(self.HEIGHT)):
            if self.board[x,column] == ' ':
                lowest = x
                break

        if lowest == -1 and self.print:
            #print("Column " + str(column + 1) + " is full!")
            #print(self.board)
            return lowest
        elif lowest == -1:
            return lowest
        else:
            return lowest
    
    def __repr__(self):
        for row in self.board:
            print(row)
        return ''

    def __str__(self):
        for row in self.board:
            print(row)
        return ''

    def counter_Check(self, win_counter):
        if win_counter == -4:
            return self.p1
        elif win_counter == 4:
            return self.p2
        else:
            return ""

    def check_win_optimized(self, column):
        # Red goes first "X"
        # Yellow goes second "O"
        win_counter = 0
        row = self.find_lowest(column) + 1
        # If the column selected has no pieces in it already it will attempt to look out of bounds,
        # one below the lowest row, so I just return false here as there is no piece here to check
        if row == 6:
            return False
        #print("WIN CHECK LOCATION: ",row, column)
        color = self.board[row,column]
        #print("COLOR ->", color, "<-")
        # If the color is blank, something bad messed up and I'm somehow checking an empty column, this shouldn't
        # happen though because of the if statement above, but keeping it here just in case
        if color == " ":
            return False
        #print("Location:", row, column)
        
        # --------------------------
        # ------- HORIZONTAL -------
        # --------------------------
        
        # Just keep going left in this row until you get win_counter to 4 (it starts at 1 for the piece just placed)
        # or you run into the opposite color
        # Keeping track of the last column there was a correct color piece, you start going back the opposite way
        # and see if there are 4 in a row going to the right
        for i in range(column + 1,self.WIDTH):
            if self.board[row,i] == color:
                #print(row, i, color)
                win_counter += 1
            else:
                break
            # If we reach 3 here, there were 4 in a row going to the right with column being the right most piece
            if win_counter == 3:
                #print("WON HORIZONTAL TO RIGHT")
                return True

        # We headed left here starting from the square to the right of the original location
        for i in reversed(range(0, column)):
            if self.board[row,i] == color:
                #print(row, i)
                win_counter += 1
            else:
                break
            if win_counter == 3:
                #print("WON HORIZONTAL TO LEFT")
                return True
        

        # ------------------------
        # ------- VERTICAL -------
        # ------------------------

        win_counter = 0
        # Same as above but instead we are looking down only in the specific column
        # We start at the location below the original spot because we know that one is of the color
        # we are looking for. This allows us to only have to look for win_counter to be 3
        ii = min(row + 1, self.HEIGHT - 1)
        while ii < self.HEIGHT:
            if self.board[ii,column] == color:
                #print(ii, column)
                win_counter += 1
            else:
                break
            if win_counter == 3:
                #print("WON VERTICAL")
                return True
            ii += 1


        # ------------------------
        # ------- DIAGONAL -------
        # ------------------------

        # Capital X is the current piece placed
        #X
        # x
        #  x
        #   x
        # This looks for the furthest you can either go down or to the right, and takes the minimum
        # so we don't go out of bounds
        furthest_distance_down_or_right = min(self.HEIGHT - row, self.WIDTH - column)
        # Now we move on to check the diagonals
        win_counter = 0
        for i in range(1,furthest_distance_down_or_right):
            if self.board[row + i,column + i] == color:
                #print(row + i, column + i)
                win_counter += 1
            else:
                break
            if win_counter == 3:
                #print("WON DIAGONAL DOWN AND RIGHT")
                return True

        # We now check from bottom right going up and left to see if there is a win in the opposite way
        # We start at the last location checked
        # We also don't need to do this loop if the previous check went down and right 3 spaces,
        # because we would just be checking the same exact spots
        win_counter == 0
        furthest_distance_up_or_left = min(row, column)
        for i in range(1, furthest_distance_up_or_left):
            if self.board[row - i,column - i] == color:
                #print(row - i, column - i)
                win_counter += 1
            else:
                break
            if win_counter == 3:
                #print("WON DIAGONAL UP AND LEFT")
                return True

        # Now we have to check down and left
        # Capital X is the current piece placed
        #   X
        #  x
        # x
        #x
                
        furthest_distance_down_or_left = min(self.HEIGHT - row, column)
        win_counter = 0
        for i in range(1,furthest_distance_down_or_left):
            if self.board[row + i,column - i] == color:
                #print(row + i, column - i)
                win_counter += 1
            else:
                break
            if win_counter == 3:
                #print("WON DIAGONAL DOWN AND LEFT")
                return True

        # Now we checking from bottom left to up right
        win_counter == 0
        furthest_distance_up_or_left = min(row, self.WIDTH - column)
        for i in range(1,furthest_distance_up_or_left):
            if self.board[row - i,column + i] == color:
                #print(row - i, column + i)
                win_counter += 1
            else:
                break
            if win_counter == 3:
                #print("WON DIAGONAL UP AND LEFT")
                return True
        return False


    def get_height(self):
            return self.HEIGHT


    def get_width(self):
        return self.WIDTH