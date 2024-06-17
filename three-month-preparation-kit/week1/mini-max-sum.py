#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minNumber=arr[0]
    maxNumber=arr[0]
    total=0
    
    for number in arr:
        if number<minNumber:
            minNumber=number
        elif number>maxNumber:
            maxNumber=number
            
        total+=number
            
    print(f'{total-maxNumber} {total-minNumber}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
