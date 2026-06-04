#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a = x1 * v2 - x2 * v1
    b = v2 - v1
    if b == 0:
        return 'YES' if a == 0 else 'NO'
    if a % b != 0:
        return 'NO'
    x = a // b
    if x < x1 or x < x2:
        return 'NO'
    if (x - x1) % v1 != 0 or (x - x2) % v2 != 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
