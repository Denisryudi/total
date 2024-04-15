#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print('Weird')
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        elif n > 20:
            print('Not Weird')

    #ou
if n % 2 != 0:
    print('Weird')
elif 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20:
    print('Weird')
else:  # This implicitly covers the case where n > 20 and n is even
    print('Not Weird')