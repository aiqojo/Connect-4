#board[row][column]


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = [['0']*width for x in range(height)]

    def add_checker(self, color, column):

        row = self.find_lowest(column - 1)

        if row == -1:
            return False
        else:
            self.board[row][column - 1] = color.upper()
            return True
    
    # Find lowest
    # If lowest isn't found, return -1, as nothing can be placed in that row
    def find_lowest(self, column):
        lowest = -1

        for x in reversed(range(self.height)):
            if self.board[x][column] == '0':
                lowest = x
                break

        if lowest == -1:
            print("Column " + str(column + 1) + " is full!")
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
            return "R"
        elif win_counter == 4:
            return "Y"
        else:
            return ""

    def check_win(self):

        # If this hits 4, win for yellow
        # If this hits -4, win for red
        win_counter = 0

        for row in reversed(range(3, self.height)):
            for column in range(self.width - 3):
                
                # Checking each row
                for x in range(4):
                    if self.board[row][column + x] == "Y":
                        win_counter += 1
                    elif self.board[row][column + x] == "R":
                        win_counter -= 1

                if self.counter_Check() == "R":
                    print("R wins!")
                elif self.counter_Check() == "Y":
                    print("Y wins!")

                win_counter = 0

                # Checking each column
                for x in range(4):
                    if self.board[row - x][column] == "Y":
                        win_counter += 1
                    elif self.board[row - x][column] == "R":
                        win_counter -= 1

                if self.counter_Check() == "R":
                    print("R wins!")
                elif self.counter_Check() == "Y":
                    print("Y wins!")

                # Checking the 2 diagonals
                for x in range(4):
                    if self.board[row - x][column + x] == "Y":
                        win_counter += 1
                    elif self.board[row + x][column - x] == "R":
                        win_counter -= 1

                if self.counter_Check() == "R":
                    print("R wins!")
                elif self.counter_Check() == "Y":
                    print("Y wins!")


    
                


        return False










