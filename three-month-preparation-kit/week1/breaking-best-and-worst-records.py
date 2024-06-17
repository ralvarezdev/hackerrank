#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    minNumber = maxNumber = scores[0]
    minBreaking = maxBreaking = 0

    for score in scores[1:]:
        if score < minNumber:
            minNumber = score
            minBreaking += 1

        elif score > maxNumber:
            maxNumber = score
            maxBreaking += 1

    return [maxBreaking, minBreaking]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
