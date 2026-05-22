#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    ans = [0] * n
    swap = [0] * n
    for i in range(n - k):
        if swap[i] or swap[i + k]:
            continue
        ans[i] = i + k
        ans[i + k] = i
        swap[i] = swap[i + k] = True

    if not all(swap):
        return [-1]
    return [x + 1 for x in ans]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
