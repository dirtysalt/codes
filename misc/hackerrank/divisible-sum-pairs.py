#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ans = 0
    from collections import Counter
    cnt = Counter()
    for x in ar:
        ans += cnt[(k * x - x) % k]
        cnt[x % k] += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
