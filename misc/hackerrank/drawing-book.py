#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if n % 2 == 0:
        a = p // 2
        b = (n - p + 1) // 2
    else:
        a = p // 2
        b = (n - p) // 2
    ans = min(a, b)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
