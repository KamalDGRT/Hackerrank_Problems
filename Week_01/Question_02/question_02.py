#!/bin/python3

# Birthday Candles Problem

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    largest = candles[0]
    index = 1
    total_candles = len(candles)

    while index < total_candles:
        candle_height = candles[index]
        if candle_height > largest:
            largest = candle_height
        index += 1

    candle_count = 0
    for candle_height in candles:
        if candle_height == largest:
            candle_count += 1    
    return candle_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
