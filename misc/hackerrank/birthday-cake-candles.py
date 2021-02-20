#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    n = len(ar)
    if n == 0:
        return 0
    ans = 1
    p = ar[0]
    for i in range(1, n):
        if p == ar[i]:
            ans += 1
        elif p < ar[i]:
            p = ar[i]
            ans = 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
