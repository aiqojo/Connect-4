import random_ai
from time import sleep

class game_handler():

    def __init__(self, board, ai_1, ai_2, delay, print):
        self.board = board
        self.ai_1 = ai_1 # red (X)
        self.ai_2 = ai_2 # yellow (O)
        self.delay = delay
        self.print = print

    def play_round(self):

        winner = ''

        while True:
            # Sentinel value
            column_choice = -1

            if self.print:
                print("Red's turn! (X)")
            #column_choice = input("Enter column: ")
            column_choice = self.ai_1.answer(self.board.find_empty_columns(), self.board)

            if self.print:
                print("RED'S CHOICE IS: ", column_choice)

            # If self.board.find_empty_columns() returns an empty list, ai_1.answer will return -1
            # This means there are no empty columns left, so a tie if a winner hasn't been found yet
            if column_choice == -1:
                if self.print:
                    print("WE HAVE TIED")
                winner = "T"
                break

            # If the board isn't full yet, put the piece in its column
            added = False
            while not added:
                added = self.board.add_checker("X", column_choice)
            
            if self.print:
                print(self.board)

            # Now check if there is a win, if so it must be red cause they just placed a piece
            if self.board.check_win():
                if self.print:
                    print("Red (X) won!")
                winner = 'X'
                break

            # Delay for easier viewing
            sleep(self.delay)

            # Same as above, just yellow's turn now
            if self.print:
                print("Yellow's turn! (O)")
            #column_choice = input("Enter column: ")
            column_choice = self.ai_2.answer(self.board.find_empty_columns(), self.board)

            if self.print:
                print("YELLOW'S CHOICE IS: ", column_choice)

            if column_choice == -1:
                if self.print:
                    print("WE HAVE TIED")
                winner = "T"
                break

            added = False
            while not added:
                added = self.board.add_checker("O", column_choice)

            if self.print:
                print(self.board)

            if self.board.check_win():
                if self.print:
                    print("Yellow (O) won!")
                winner = 'O'
                break

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

    