#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the solve function below.
def solve(a):
    from collections import Counter
    cnt = Counter()
    for x in a:
        cnt[x] += 1
    ans = 0
    for x, c in cnt.items():
        ans += c * (c - 1)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
