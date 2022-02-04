from random_ai import random_ai


# random, 
class ai_handler():
    
    def __init__(self, ai):
        if ai == "random":
            self.ai = random_ai()
    

    def answer(self, width):
        return random_ai.answer(width)



