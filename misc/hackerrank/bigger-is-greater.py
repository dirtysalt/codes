#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)
    n = len(w)

    max_idx = n - 1
    p = -1
    for i in reversed(range(n)):
        if w[i] < w[max_idx]:
            p = i
            break
        max_idx = i

    if p == -1:
        return "no answer"

    min_idx = p + 1
    for i in range(p + 1, n):
        if w[i] > w[p] and w[i] < w[min_idx]:
            min_idx = i

    w[p], w[min_idx] = w[min_idx], w[p]
    w[p + 1:] = sorted(w[p + 1:])
    ans = ''.join(w)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
