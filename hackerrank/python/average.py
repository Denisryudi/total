#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*nums):
    average = sum(nums) / len(nums)
    return average


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    res = avg(*nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()