from multiprocessing.connection import answer_challenge
import random

class random_ai:

    def answer(self, arr):
        #print("AI CHOICE ARRAY: ", arr)

        if len(arr) == 0:
            return -1
        else:
            return random.choice(arr)





