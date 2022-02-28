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
        self.lowest_row = np.full((1,7), 5)
        
        self.zArray = np.random.randint(sys.maxsize, size=(2,6,7), dtype=np.uint64)

        self.board_history = ''

        self.find_lowest_count = 0
        self.add_piece_count = 0
        self.remove_piece_count = 0
        self.find_empty_columns_count = 0
        self.check_win_optimized_count = 0

    def reset(self):
        if self.print:
            print("-------NEW GAME-------")
        self.board = np.zeros((6,7), dtype='str')
        self.board[:] = ' '
        self.board_history = ''
        self.lowest_row = np.full((1,7), 5)

    def __key(self):
        pass
        #return key

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.__key() == other.__key()
        return NotImplemented


    def get_board_state(self):
        return self.board_history


    def add_piece(self, color, column):
        #print(self.lowest_row)
        self.add_piece_count += 1
        #column = int(column)
        row = self.lowest_row[0,column]
        if row == -1:
            return False
        else:
            self.board[row,column] = color.upper()
            self.lowest_row[0,column] -= 1
            return True

    def remove_piece(self,column):
        self.remove_piece_count += 1
        row = self.lowest_row[0,column] + 1
        if row > 5:
            return False
        else:
            self.board[row,column] = ' '
            self.lowest_row[0,column] += 1
            return True


    def find_empty_columns(self):
        self.find_empty_columns_count += 1
        arr = list(range(0, self.WIDTH))
        arrr = []

        for x in arr:
            if self.board[0, x] == ' ':
                arrr.append(x)
        #print("Column choices:", arrr)
        return arrr


    def get_location_color(self, row, column):
        return self.board[row,column]

    
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
        self.check_win_optimized_count += 1
        # Red goes first "X"
        # Yellow goes second "O"
        win_counter = 0
        row = self.lowest_row[0,column] + 1
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
        furthest_distance = min(self.HEIGHT - row, self.WIDTH - column)
        # Now we move on to check the diagonals
        win_counter = 0
        for i in range(1,furthest_distance):
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
        furthest_distance = min(row, column) + 1
        for i in range(1, furthest_distance):
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
        
        furthest_distance = min(self.HEIGHT - row - 1, column) + 1
        win_counter = 0

        for i in range(1,furthest_distance):
            #print(row + i, column - i)
            if self.board[row + i,column - i] == color:
                win_counter += 1
                #print("COLOR",row + i, column - i, win_counter)
            else:
                break
            if win_counter == 3:
                #print("WON DIAGONAL DOWN AND LEFT")
                return True

        # Now we checking from bottom left to up right

        furthest_distance = min(row, self.WIDTH - column - 1) + 1
        for i in range(1,furthest_distance):
            #print(row - i, column + i)
            if self.board[row - i,column + i] == color:
                win_counter += 1
                #print("COLOR ",row - i, column + i, win_counter)
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
        