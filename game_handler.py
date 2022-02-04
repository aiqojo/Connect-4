import random_ai
from time import sleep

class game_handler():

    def __init__(self, board, ai, delay):
        self.board = board
        self.ai = ai
        self.delay = delay


    def play(self):

        winner = ''

        while True:
            value = -1

            print("Red's turn!")
            #value = input("Enter column: ")
            value = self.ai.answer(self.board.find_empty_columns())

            if value == 

            self.board.add_checker("r", value)
            print(self.board)

            if self.board.check_win():
                winner = 'R'
                break

            sleep(self.delay)

            print("Yellow's turn!")
            #value = input("Enter column: ")
            value = self.randy.answer(self.width)
            self.board.add_checker("y", value)
            print(self.board)

            if self.board.check_win():
                winner = 'Y'
                break

            sleep(self.delay)

        return winner

    