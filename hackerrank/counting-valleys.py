#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    h = 0
    ans = 0
    for c in s:
        if c == 'U':
            h += 1
        else:
            h = h - 1
            if h == -1:
                ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
