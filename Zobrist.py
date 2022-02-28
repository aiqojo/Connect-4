import numpy as np
from random import *
import sys

class Zobrist():
    zArray = np.random.randint(sys.maxsize, size=(2,6,7), dtype=np.uint64)
    print(zArray)

    def get_zhash():
        returnZKey = 0
    
    
