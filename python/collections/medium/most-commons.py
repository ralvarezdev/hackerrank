#!/bin/python3

from collections import OrderedDict
from functools import cmp_to_key

def compare(a, b):
    return ord(a[0]) - ord(b[0]) if a[1] == b[1] else b[1] - a[1]

if __name__ == '__main__':
    s = input()

    letters = OrderedDict()
    for letter in s:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1

    lettersList = [[key, letters[key]] for key in letters.keys()]
    lettersList.sort(key=cmp_to_key(compare))

    for letter in lettersList[:3]:
        print(" ".join(map(str, letter)))
