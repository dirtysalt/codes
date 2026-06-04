#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os
from collections import Counter


# Complete the maxRegion function below.
def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    mask = []
    for i in range(n):
        mask.append([0] * m)

    regid = 1

    def dfs(i, j):
        if not grid[i][j] or mask[i][j]:
            return

        mask[i][j] = regid
        for (di, dj) in [(x, y) for x in range(-1, 2) for y in range(-1, 2)]:
            if di == 0 and dj == 0:
                continue
            if (di + i) >= 0 and (di + i) < n and \
                            (dj + j) >= 0 and (dj + j) < m:
                dfs(di + i, dj + j)

    for i in range(n):
        for j in range(m):
            if grid[i][j] and not mask[i][j]:
                dfs(i, j)
                regid += 1

    counter = Counter()
    for i in range(n):
        for j in range(m):
            if mask[i][j]:
                counter[mask[i][j]] += 1

    top = counter.most_common(1)
    return top[0][1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
