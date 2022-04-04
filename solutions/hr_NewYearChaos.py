#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    move = 0
    moves = {n: 0 for n in q}
    step = 0
    currentstep = 1
    i = 0
    while currentstep > 0:
        currentstep = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                moves[q[i]] += 1
                if moves[q[i]] > 2:
                    print('Too chaotic')
                    return
                q[i], q[i + 1] = q[i + 1], q[i]
                step += 1
                currentstep += 1
    print(step)
    return


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
