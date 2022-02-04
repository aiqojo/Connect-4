from random_ai import random_ai
from time import sleep

# random, 
class ai_handler():
    
    def __init__(self, ai):
        if ai == "random":
            self.ai = random_ai()
        self.timer = 0
    

    def answer(self, arr):
        return self.ai.answer(arr)

    # def set_timer(self, seconds):
    #     self.seconds = seconds

    # def check_timer(self):
    #     if self.timer > 0:
    #         sleep(self.timer)
    #     else:
    #         pass

