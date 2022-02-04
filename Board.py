#board[row][column]


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = [['.']*width for x in range(height)]

    # column is "human" row, starting from 1 not 0
    def add_checker(self, color, column):

        column = int(column)

        # subtracting 1 
        row = self.find_lowest(column - 1)

        if row == -1:
            return False
        else:
            self.board[row][column - 1] = color.upper()
            return True

    def find_empty_columns(self):
        arr = list(range(0, self.width))

        for x in arr:
            if self.find_lowest(x) == '-1':
                arr.remove(x)
        
        return arr


    # Find lowest
    # If lowest isn't found, return -1, as nothing can be placed in that row
    def find_lowest(self, column):
        lowest = -1

        for x in reversed(range(self.height)):
            if self.board[x][column] == '.':
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
                    for y in range(4):
                        if self.board[row - x][column + y] == "Y":
                            win_counter += 1
                        elif self.board[row - x][column + y] == "R":
                            win_counter -= 1

                    if self.counter_Check(win_counter) == "R":
                        print("R wins!")
                        return True
                    elif self.counter_Check(win_counter) == "Y":
                        print("Y wins!")
                        return True
                    
                    win_counter = 0


                # Checking each column
                for x in range(4):
                    for y in range(4):
                        if self.board[row - y][column + x] == "Y":
                            win_counter += 1
                        elif self.board[row - y][column + x] == "R":
                            win_counter -= 1

                    if self.counter_Check(win_counter) == "R":
                        print("R wins!")
                        return True
                    elif self.counter_Check(win_counter) == "Y":
                        print("Y wins!")
                        return True
                    win_counter = 0

                win_counter = 0


                # Checking the 2 diagonals
                for x in range(4):
                    if self.board[row - x][column + x] == "Y":
                        win_counter += 1
                    if self.board[row - x][column + x] == "R":
                        win_counter -= 1
                
                if self.counter_Check(win_counter) == "R":
                    print("R wins!")
                    return True
                elif self.counter_Check(win_counter) == "Y":
                    print("Y wins!")
                    return True

                win_counter = 0

                for x in range(4):
                    if self.board[row - 3 + x][column + x] == "Y":
                        win_counter += 1
                    if self.board[row - 3 + x][column + x] == "R":
                        win_counter -= 1

                if self.counter_Check(win_counter) == "R":
                    print("R wins!")
                    return True
                elif self.counter_Check(win_counter) == "Y":
                    print("Y wins!")
                    return True

                win_counter = 0                


        return False
