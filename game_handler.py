import random_ai
from time import sleep

class game_handler():

    def __init__(self, board, red, yellow, delay, print):
        self.board = board
        self.red = red # red (X)
        self.yellow = yellow # yellow (O)
        self.delay = delay
        self.print = print
        self.first = False

    def play_round(self):
        
        if self.print and not self.first:
            print("----NEW GAME----")
            print(self.board)
        elif self.print:
            print(self.board)
        
        self.first = True

        winner = ''

        while True:
            # Sentinel value
            column_choice = -1

            if self.print:
                print("Red's turn! (X)")
            #column_choice = input("Enter column: ")
            column_choice = self.red.get_answer(self.board.find_empty_columns(), self.board)

            if self.print:
                print("RED'S CHOICE IS:", column_choice)

            # If self.board.find_empty_columns() returns an empty list, red.answer will return -1
            # This means there are no empty columns left, so a tie if a winner hasn't been found yet
            if column_choice == -1:
                if self.print:
                    print("WE HAVE TIED")
                winner = "T"
                break
            else:
                # If the board isn't full yet, put the piece in its column
                self.board.add_piece("X", column_choice)
                if self.print:
                    print(self.board)

            # Now check if there is a win, if so it must be red cause they just placed a piece
            # if self.board.check_win():
            #     if self.print:
            #         print("Red (X) won!")
            #     winner = 'X'
            #     break

            if self.board.check_win_optimized(column_choice):
                if self.print:
                    print("Red (X) won!")
                winner = 'X'
                break

            # Delay for easier viewing
            if self.delay != 0:
                sleep(self.delay)

            # Same as above, just yellow's turn now
            if self.print:
                print("Yellow's turn! (O)")
            #column_choice = input("Enter column: ")
            column_choice = self.yellow.get_answer(self.board.find_empty_columns(), self.board)

            if self.print:
                print("YELLOW'S CHOICE IS:", column_choice)

            if column_choice == -1:
                if self.print:
                    print("WE HAVE TIED")
                winner = "T"
                break
            else:
                self.board.add_piece("O", column_choice)
                if self.print:
                    print(self.board)

            # if self.board.check_win():
            #     if self.print:
            #         print("Yellow (O) won!")
            #     winner = 'O'
            #     break

            if self.board.check_win_optimized(column_choice):
                if self.print:
                    print("Yellow (O) won!")
                winner = 'O'
                break

            # Delay for easier viewing
            if self.delay != 0:
                sleep(self.delay)

        if self.print:
            if winner == "X":
                print("RED WON")
            elif winner == "O":
                print("YELLOW WON")
            else:
                print("TIEEEEEE")
            print(self.board)

        return winner

    