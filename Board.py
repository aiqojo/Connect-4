#board[row][column]


class Board:

    p1 = "X"
    p2 = "O"

    def __init__(self, width, height, print):
        self.width = width
        self.height = height
        self.print = print

        self.board = [['.']*width for x in range(height)]

    def reset(self):
        if self.print:
            print("-------NEW GAME-------")
        self.board = [['.']*self.width for x in range(self.height)]

    def add_checker(self, color, column):

        column = int(column)

        row = self.find_lowest(column)

        if row == -1:
            return False
        else:
            if self.print:
                print("COLOR:", color, "ROW:", row, "COLUMN:", column)
            self.board[row][column] = color.upper()
            return True

    def find_empty_columns(self):
        arr = list(range(0, self.width))
        arrr = []

        for x in arr:
            if not self.find_lowest(x) == -1:
                arrr.append(x)
        
        return arrr


    # Find lowest
    # If lowest isn't found, return -1, as nothing can be placed in that row
    def find_lowest(self, column):
        lowest = -1

        for x in reversed(range(self.height)):
            if self.board[x][column] == '.':
                lowest = x
                break

        if lowest == -1 and self.print:
            print("Column " + str(column + 1) + " is full!")
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

    def check_win(self):

        # If this hits -4, win for red (p1)
        # If this hits 4, win for yellow (p2)
        win_counter = 0

        for row in reversed(range(3, self.height)):
            for column in range(self.width - 3):

                # Checking each row
                for x in range(4):
                    for y in range(4):
                        if self.board[row - x][column + y] == self.p1:
                            win_counter -= 1
                        elif self.board[row - x][column + y] == self.p2:
                            win_counter += 1

                    if self.counter_Check(win_counter) == self.p1:
                        if self.print:
                            print("Red (X) wins!")
                        return True
                    elif self.counter_Check(win_counter) == self.p2:
                        if self.print:
                            print("Yellow (O) wins!")
                        return True
                    
                    win_counter = 0


                # Checking each column
                for x in range(4):
                    for y in range(4):
                        if self.board[row - y][column + x] == self.p1:
                            win_counter -= 1
                        elif self.board[row - y][column + x] == self.p2:
                            win_counter += 1

                    if self.counter_Check(win_counter) == self.p1:
                        if self.print:
                            print("Red (X) wins!")
                        return True
                    elif self.counter_Check(win_counter) == self.p2:
                        if self.print:
                            print("Yellow (O) wins!")
                        return True
                    win_counter = 0

                win_counter = 0


                # Checking the 2 diagonals
                for x in range(4):
                    if self.board[row - x][column + x] == self.p1:
                        win_counter -= 1
                    if self.board[row - x][column + x] == self.p2:
                        win_counter += 1
                
                if self.counter_Check(win_counter) == self.p1:
                    if self.print:
                        print("Red (X) wins!")
                    return True
                elif self.counter_Check(win_counter) == self.p2:
                    if self.print:
                        print("Yellow (O) wins!")
                    return True

                win_counter = 0

                for x in range(4):
                    if self.board[row - 3 + x][column + x] == self.p1:
                        win_counter -= 1
                    if self.board[row - 3 + x][column + x] == self.p2:
                        win_counter += 1

                if self.counter_Check(win_counter) == self.p1:
                    if self.print:
                        print("Red (X) wins!")
                    return True
                elif self.counter_Check(win_counter) == self.p2:
                    if self.print:
                        print("Yellow (O) wins!")
                    return True

                win_counter = 0                


        return False
