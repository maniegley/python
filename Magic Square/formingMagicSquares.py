# Forming Magic Square

import math
import os
import random
import re
import sys
from itertools import *
# Complete the formingMagicSquare function below.
def formingMagicSquare():
    magicSquares = []  
 
    for P in permutations(range(1,10)):
        
        if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
            square = [P[0:3], P[3:6], P[6:9]]
	    magicSquares.append(square)
    return magicSquares

if __name__ == '__main__':
    
    i = 1
    result = formingMagicSquare()

    for square in result:
        print("Magic Square",i)
        for el in square:
            print(el[0], el[1], el[2])

