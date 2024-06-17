#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    numberLength=len(arr)
    positiveCounter=0
    negativeCounter=0
    ceroCounter=0
    
    for number in arr:
        if number>0:
            positiveCounter+=1
        elif number<0:
            negativeCounter+=1
        else:
            ceroCounter+=1
        
    for number in [positiveCounter, negativeCounter, ceroCounter]:
        print(number/numberLength)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)