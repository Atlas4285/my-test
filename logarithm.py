# logarithm.py

import math

def logarithm(a, base=math.e):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values!")
    return math.log(a, base)
