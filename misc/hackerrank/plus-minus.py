#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    N = len(arr)
    p, n, z = 0, 0, 0
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1

    def pr(v, n):
        scale = 1000000
        v = v * scale / n
        v = v / scale
        return '{:0.6f}'.format(v)
    print(pr(p, N))
    print(pr(n, N))
    print(pr(z, N))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
