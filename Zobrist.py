import numpy as np
import sys

class Zobrist():

    def __init__(self):
        self.zArray = np.random.randint(sys.maxsize, size=(6,7,2), dtype=np.uint64)
        self.zHash = 0
        self.board_table = {}

    def clear(self):
        print(self.board_table)
        self.board_table = {}

    