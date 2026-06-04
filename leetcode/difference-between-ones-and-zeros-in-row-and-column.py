#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        diff = [[0] * m for _ in range(n)]
        rows = [0] * n
        cols = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                else:
                    rows[i] -= 1
                    cols[j] -= 1

        for i in range(n):
            for j in range(m):
                diff[i][j] = rows[i] + cols[j]

        return diff


if __name__ == '__main__':
    pass
