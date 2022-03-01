from random_ai import random_ai
from time import sleep
from player import player
from randosmart_ai import randosmart_ai
from miniminimax import miniminimax

# random, 
class ai_handler:
    
    def __init__(self, ai, color, depth):
        if ai == "player":
            self.ai = player(color)
        elif ai == "randy":
            self.ai = random_ai(color)
        elif ai == "randosmart":
            self.ai = randosmart_ai(color)
        elif ai == "miniminimax":
            self.ai = miniminimax(color, depth)

    def get_answer(self, arr, board, zobrist):
        return self.ai.answer(arr, board, zobrist)
