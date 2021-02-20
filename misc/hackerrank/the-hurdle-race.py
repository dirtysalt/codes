#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the hurdleRace function below.
def hurdleRace(k, height):
    ans = max(0, max(height) - k)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
