import numpy as np
import sys

class Zobrist():

    def __init__(self):
        self.zArray = np.random.randint(sys.maxsize, size=(6,7,2), dtype=np.uint64)
        self.zHash = 0
        self.board_table = {}
        self.count = 0

    def clear(self):
        self.count = 0
        #print("ZOBRIST COUNT",self.count)
        self.board_table = {}

    

    