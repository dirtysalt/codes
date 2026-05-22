#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    sz = len(s)
    rem = n % sz
    a, b = 0, 0
    for i in range(sz):
        if s[i] == 'a':
            if (rem - 1) >= i:
                b += 1
            a += 1
    ans = (n // sz) * a + b
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
