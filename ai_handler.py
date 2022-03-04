from mediminimax import mediminimax
from random_ai import random_ai
from time import sleep
from player import player
from randosmart_ai import randosmart_ai
from miniminimax import miniminimax

# random, 
class ai_handler:
    
    def __init__(self, ai, color, depth):
        if ai == "player":
            self.name = "player"
            self.ai = player(color)
        elif ai == "randy":
            self.name = "random_ai"
            self.ai = random_ai(color)
        elif ai == "randosmart":
            self.name = "randosmart"
            self.ai = randosmart_ai(color)
        elif ai == "miniminimax":
            self.name = "miniminimax"
            self.ai = miniminimax(color, depth)
        elif ai == "mediminimax":
            self.name = "mediminimax"
            self.ai = mediminimax(color, depth)

    def get_answer(self, arr, board, zobrist):
        return self.ai.answer(arr, board, zobrist)
