import random

# This ai will place pieces at random, but if it sees that it can win next turn with a move 
# it will make that move
class randosmart_ai:

    # Color is either "X" for red, or "O" for yellow
    def __init__(self, color):
        self.color = color

        if color == "X":
            self.opposite_color = "O"
        else:
            self.opposite_color = "X"

    def counter_check(self, counter):
        if self.color == "X":
            if counter == -4:
                return True
        elif self.color == "O":
            if counter == 4:
                return True
        else:
            return False

    def block_or_win(self, num):
        if num == -3:
            return "b"
        elif num == 3:
            return "w"


    # Takes in array of possible columns as well as the board
    def answer(self, arr, board):

        random.seed()

        #print("AI CHOICES:", arr)

        win_counter = 0

        for row in reversed(range(2, board.get_height())):
            for column in range(board.get_width() - 2):

                # Checking if there can be a connect 4 horizontally
                for x in range(3):
                    for y in range(3):
                        if board.get_location_color(row - x, column + y) == self.color:
                        #if board[row - x][column + y] == self.color:
                            win_counter += 1
                        elif board.get_location_color(row - x, column + y) == self.opposite_color:
                        #if board[row - x][column + y] == self.color:
                            win_counter -= 1

                    #if win_counter == 3 or win_counter == -3:
                        #print("Origin:", row, column, "Horiztonal win counter at:", win_counter)

                    if win_counter == 3 or win_counter == -3:
                        # Checking column before original, making sure it is in bounds
                        # And making sure the lowest is the row it is on
                        if column - 1 >= 0 and board.find_lowest(column - 1) == row - x:
                            #print("Column/Lowest Row", column - 1, row - x)
                            if column - 1 in arr:
                                return column - 1
                        # Checking column after last
                        elif column + 3 <= 6 and board.find_lowest(column + 3) == row - x:
                            #print("Column/Lowest Row", column + 3, row - x)
                            if column + 1 in arr:
                                return column + 3

                    # Reset win counter so it doesn't carry over
                    win_counter = 0


                # Checking if there can be a connect 4 vertically
                for x in range(3):
                    for y in range(3):
                        if board.get_location_color(row - y, column + x) == self.color:
                        #if self.board[row - y][column + x] == self.color:
                            win_counter += 1
                        elif board.get_location_color(row - y, column + x) == self.opposite_color:
                            win_counter -= 1

                    #if win_counter == 3 or win_counter == -3:
                        #print("Origin:", row, column, "Vertical win counter at:", win_counter)

                    # If the counter has seen three in a row going up or down
                    if win_counter == 3 or win_counter == -3:
                        # Check to see if next is empty
                        if board.find_lowest(column + x) == row - y - 1:
                            #print("Column/Lowest Row", column + x, row - y - 1)
                            # Return correct column
                            if column + x in arr:
                                return column + x

                    # Reset win counter so it doesn't carry over
                    win_counter = 0      


                # Checking diagonals
                for x in range(3):
                    if board.get_location_color(row - x, column + x) == self.color:
                    #if self.board[row - x][column + x] == self.color:
                        win_counter += 1
                    elif board.get_location_color(row - x, column + x) == self.opposite_color:
                        win_counter -= 1

                    #if win_counter == 3 or win_counter == -3:
                        #print("Origin:", row, column, "Diagonal (bleft-tright) win counter at:", win_counter)

                    if win_counter == 3 or win_counter == -3:
                        # Checking column before original, making sure it is in bounds
                        # And making sure the lowest is the row 1 lower than the origin
                        # Looking at location O 
                        #|~|~|~|X|
                        #|~|~|X|~|
                        #|~|X|~|~|
                        #|O|~|~|~|
                        if column + x - 3 >= 0 and board.find_lowest(column + x - 3) == row + 1:
                            #print("Column/Lowest Row", column + x - 3, row + 1)
                            if column + x - 3 in arr:
                                return column + x - 3
                        # Checking column after last and making sure the lowest is one higher
                        # Looking at location O
                        #|~|~|~|O|
                        #|~|~|X|~|
                        #|~|X|~|~|
                        #|X|~|~|~|
                        elif column + x + 1 <= 6 and board.find_lowest(column + x + 1) == row - 1:
                            #print("Column/Lowest Row", column + x + 1, row - 1)
                            if column + x + 1 in arr:
                                return column + x + 1

                win_counter = 0

                for x in reversed(range(3)):
                    if board.get_location_color(row - x, column + 2 - x) == self.color:
                    #if self.board[row - x][column + x] == self.color:
                        win_counter += 1
                    elif board.get_location_color(row - x, column + 2 - x) == self.color:
                        win_counter -= 1

                    #if win_counter == 3 or win_counter == -3:
                    #    print("Origin:", row, column, "Diagonal (tleft-bright) win counter at:", win_counter)

                    if win_counter == 3 or win_counter == -3:
                        # Checking column before original, making sure it is in bounds
                        # And making sure the lowest is the row 1 lower than the origin
                        # Looking at location O, starting at capital X
                        #|O|~|~|~|
                        #|~|X|~|~|
                        #|~|~|x|~|
                        #|~|~|~|x|
                        if column - 1 >= 0 and board.find_lowest(column - 1) == row - 1 >= 0:
                            #print("Column/Lowest Row", column - 1, row - 1)
                            if column + x - 3 in arr:
                                return column + x - 3
                        # Checking column after last and making sure the lowest is one higher
                        # Looking at location O
                        #|X|~|~|~|
                        #|~|x|~|~|
                        #|~|~|x|~|
                        #|~|~|~|O|
                        elif column + 3 <= 6 and board.find_lowest(column + 3) == row + 3 and row + 3 <= 5:
                            #print("Column/Lowest Row", column + 3, row + 3)
                            if column + 3 in arr:
                                return column + 3

        if len(arr) == 0:
            return -1
        else:
            return random.choice(arr)
