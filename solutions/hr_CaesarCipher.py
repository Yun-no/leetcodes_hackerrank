#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    input = list(s)
    output = ''
    for c in input:
        if c.lower() in alphabet:
            output += shiftLetter(c,k,alphabet)
        else:
            output += c
    return output
    # Write your code here


def shiftLetter(c,k,a):
    if c.isupper():
        c = c.lower()
        p = a.index(c)
        i = p + k
        if i > len(a) - 1:
            while i >= len(a):
                i = i - len(a)
        return a[i].upper()
    else:
        p = a.index(c)
        i = p + k
        if i > len(a) - 1:
            while i >= len(a):
                i = i - len(a)
        return a[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
