import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    message = ""
    if n % 2:
        message = "Weird"
    else:
        if n >= 2 and n <= 5:
            message = "Not Weird"
        elif n >= 6 and n <= 20:
            message = "Weird"
        else:
            message = "Not Weird"
    print(message)
