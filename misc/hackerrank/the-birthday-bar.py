#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the birthday function below.
def birthday(s, d, m):
    ans = 0
    if len(s) < m:
        return ans

    x = sum(s[:m])
    if x == d:
        ans += 1

    for i in range(m, len(s)):
        x += s[i]
        x -= s[i - m]
        if x == d:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
