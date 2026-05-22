#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    xs = x
    xs.sort()
    n = len(xs)

    right = [-1] * n
    j = n - 1
    for i in reversed(range(n)):
        while j >= i and xs[j] - xs[i] > k:
            j -= 1
        right[i] = j

    ans = 0
    i = 0
    while i < n:
        i = right[i]
        # print('put ', i)
        ans += 1
        i = right[i]
        i = i + 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
