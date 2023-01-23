#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the surfaceArea function below.
def surfaceArea(A):
    def transpose(A):
        return list(zip(*A))

    def area(A):
        n, m = len(A), len(A[0])
        res = 0
        for i in range(n):
            h = 0
            for j in range(m):
                delta = A[i][j] - h
                if delta > 0:
                    res += delta
                h = A[i][j]
        return res

    n, m = len(A), len(A[0])
    ans = 0
    ans += 2 * n * m
    for i in range(4):
        A = transpose(A)
        ans += area(A)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
