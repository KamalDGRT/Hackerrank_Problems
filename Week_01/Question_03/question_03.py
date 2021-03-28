#!/bin/python3

# Alternating Characters

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    index = 1
    length = len(s)
    duplicate_count = 0
    while index < length:
        current_char = s[index]
        previous_char = s[index - 1]
        if current_char == previous_char:
            duplicate_count += 1
            index += 1
            continue
        index += 1
    return duplicate_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
