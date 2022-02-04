from multiprocessing.connection import answer_challenge
import random

class random_ai:

    def answer(self, arr):

        if len(arr) == 0:
            return -1
        else:
            return random.choice(arr)





