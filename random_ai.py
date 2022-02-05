from multiprocessing.connection import answer_challenge
import random

# This ai chooses a random column from those that are available
class random_ai:

    def __init__(self, color):
        self.color = color

    def answer(self, arr, board):
        #print("AI CHOICE ARRAY: ", arr)

        if len(arr) == 0:
            return -1
        else:
            return random.choice(arr)





