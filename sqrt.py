# sqrt.py

import math

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number!")
    return math.sqrt(a)
