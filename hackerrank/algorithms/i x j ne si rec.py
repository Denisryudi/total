#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'nearlySimilarRectangles' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_LONG_INTEGER_ARRAY sides as parameter.
#

def nearlySimilarRectangles(sides):
    # Write your code here

    similar = 0
    for i in range(0, len(sides) - 1):
        x = sides[i]
        for j in range(i + 1, len(sides)):
            y = sides[j]

            if x[0] * y[1] == x[1] * y[0]:
                similar += 1
    return similar

#on^2 preciso ajustar



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []

    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)

    fptr.write(str(result) + '\n')

    fptr.close()