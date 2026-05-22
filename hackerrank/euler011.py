#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(grid):
    n = 20
    max_res = 0
    for i in range(0, n):
        for j in range(0, n):
            if (i + 3) < n:
                res = 1
                for x in range(0, 4):
                    res *= grid[i + x][j]
                if res > max_res:
                    max_res = res
            if (j + 3) < n:
                res = 1
                for x in range(0, 4):
                    res *= grid[i][j + x]
                if res > max_res:
                    max_res = res
            if (i + 3) < n and (j + 3) < n:
                res = 1
                for x in range(0, 4):
                    res *= grid[i + x][j + x]
                if res > max_res:
                    max_res = res
            if (i + 3) < n and (j - 3) >= 0:
                res = 1
                for x in range(0, 4):
                    res *= grid[i + x][j - x]
                if res > max_res:
                    max_res = res
    return max_res


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
print((solve(grid)))
