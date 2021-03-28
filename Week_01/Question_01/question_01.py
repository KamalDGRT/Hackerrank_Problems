#!/bin/python3

# Staircase Problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    steps = n - 1
    charcount = 1
    while steps >= 0:
        for space in range(steps):
            print(' ', end='')
        for number in range(charcount):
            print('#', end='')
        print('')
        steps -= 1
        charcount += 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
