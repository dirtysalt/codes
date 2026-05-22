#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the organizingContainers function below.
def organizingContainers(container):
    n = len(container)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        for j in range(n):
            a[i] += container[i][j]
            b[j] += container[i][j]

    a.sort()
    b.sort()
    ok = (a == b)
    ans = 'Possible' if ok else 'Impossible'
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
