#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    newWord=True
    counter=0

    for c in s:
        if newWord and not c.isspace() and c.isalpha():
            s=s[:counter]+c.upper()+s[counter+1:]
            newWord=False

        counter+=1
        newWord=c.isspace()

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
