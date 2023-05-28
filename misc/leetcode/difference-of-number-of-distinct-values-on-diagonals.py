#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]

        def check(x, y, dx, dy):
            rr = set()
            while True:
                x, y = x + dx, y + dy
                if 0 <= x < n and 0 <= y < m:
                    rr.add(grid[x][y])
                else:
                    break
            return len(rr)

        for i in range(n):
            for j in range(m):
                a = check(i, j, -1, -1)
                b = check(i, j, 1, 1)
                ans[i][j] = abs(a - b)
        return ans


if __name__ == '__main__':
    pass
