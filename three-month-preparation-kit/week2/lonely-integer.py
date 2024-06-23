#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    elementCounter = dict()

    for element in a:
        if element not in elementCounter:
            elementCounter[element] = 1
        else:
            elementCounter[element] = elementCounter[element] + 1

    for [key, value] in elementCounter.items():
        if value == 1:
            return key


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + "\n")

    fptr.close()
