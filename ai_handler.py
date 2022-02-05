from random_ai import random_ai
from time import sleep
from player import player
from randosmart_ai import randosmart_ai

# random, 
class ai_handler():
    
    def __init__(self, ai, colors, which_color):
        if ai == "player":
            self.ai = player(colors[which_color])
        elif ai == "randy":
            self.ai = random_ai(colors[which_color])
        elif ai == "randosmart":
            self.ai = randosmart_ai(colors[which_color])
        self.timer = 0
    

    def answer(self, arr, board):
        return self.ai.answer(arr, board)

    # def set_timer(self, seconds):
    #     self.seconds = seconds

    # def check_timer(self):
    #     if self.timer > 0:
    #         sleep(self.timer)
    #     else:
    #         pass

