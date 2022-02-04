import random_ai
from time import sleep

class game_handler():

    def __init__(self, board, ai_1, ai_2, delay):
        self.board = board
        self.ai_1 = ai_1
        self.ai_2 = ai_2
        self.delay = delay


    def play_round(self):

        winner = ''

        while True:
            value = -1

            print("Red's turn! (X)")
            #value = input("Enter column: ")
            value = self.ai_1.answer(self.board.find_empty_columns())

            # If self.board.find_empty_columns() returns an empty list, ai_1.answer will return -1
            # This means there are no empty columns left, so a tie if a winner hasn't been found yet
            if value == -1:
                winner = "Tie"
                break

            # If the board isn't full yet, put the piece in its column
            self.board.add_checker("x", value)
            print(self.board)

            # Now check if there is a win, if so it must be red cause they just placed a piece
            if self.board.check_win():
                winner = 'x'
                break

            # Delay for easier viewing
            sleep(self.delay)

            # Same as above, just yellow's turn now
            print("Yellow's turn! (O)")
            #value = input("Enter column: ")
            value = self.ai_2.answer(self.board.find_empty_columns())

            if value == -1:
                winner = "T"
                break

            self.board.add_checker("o", value)
            print(self.board)

            if self.board.check_win():
                winner = 'O'
                break

            sleep(self.delay)

        return winner

    