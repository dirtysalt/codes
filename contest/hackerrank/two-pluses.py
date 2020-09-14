#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the twoPluses function below.
def twoPluses(grid):
    n, m = len(grid), len(grid[0])

    def outers(x, y, k):
        tmp = []
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            tx, ty = x + dx * k, y + dy * k
            if 0 <= tx < n and 0 <= ty < m and grid[tx][ty] == 'G':
                tmp.append((tx, ty))
        return tmp

    def max_area(x, y, x2, y2):
        ans = 0
        cs = set()
        for k in range(n):
            tmp = outers(x, y, k)
            if len(tmp) != 4:
                break
            cs.update(tmp)
            sz1 = 4 * k + 1

            for k2 in range(n):
                tmp2 = outers(x2, y2, k2)
                if len(tmp2) != 4:
                    break
                if set(tmp2) & cs:
                    break

                sz2 = 4 * k2 + 1
                ans = max(ans, sz1 * sz2)
        return ans

    xys = [(x, y) for x in range(n) for y in range(m)]
    N = len(xys)
    assert N == n * m
    ans = 0
    for i in range(N):
        x, y = xys[i]
        if grid[x][y] != 'G': continue
        for j in range(i + 1, N):
            x2, y2 = xys[j]
            if grid[x2][y2] != 'G': continue
            value = max_area(x, y, x2, y2)
            ans = max(ans, value)
    return ans


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
