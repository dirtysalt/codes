#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the encryption function below.
def encryption(s):
    L = len(s)
    n = m = int(L ** 0.5 + 0.5)
    if n * n < L:
        m = n + 1

    start = 0
    idx = start
    ans = ''
    for i in range(L):
        ans += s[idx]
        idx += m
        if idx >= L:
            start += 1
            idx = start
            ans += ' '
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
