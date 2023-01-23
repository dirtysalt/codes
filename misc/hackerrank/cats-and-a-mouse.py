#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    a, b = abs(x - z), abs(y - z)
    if a < b:
        return 'Cat A'
    elif a > b:
        return 'Cat B'
    else:
        return 'Mouse C'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
