#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the breakingRecords function below.
def breakingRecords(scores):
    a = b = scores[0]
    t0 = t1 = 0
    for x in scores:
        if x > a:
            t0 += 1
            a = x
        if x < b:
            t1 += 1
            b = x
    return t0, t1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
