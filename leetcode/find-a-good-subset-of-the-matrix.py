#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ok = set()
        for i in range(1 << n):
            for j in range(1 << n):
                if (i & j) == 0:
                    ok.add((i, j))

        pos = [[] for _ in range(1 << n)]
        m = len(grid)
        for i in range(m):
            value = 0
            for x in grid[i]:
                value = (value << 1) | x
            pos[value].append(i)

        if pos[0]:
            return [pos[0][0]]

        for x, y in ok:
            if pos[x] and pos[y]:
                ans = [pos[x][0], pos[y][0]]
                ans.sort()
                return ans

        return []


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]], [0, 1]),
    ([[0]], [0]),
    ([[1, 1, 1], [1, 1, 1]], []),
]

aatest_helper.run_test_cases(Solution().goodSubsetofBinaryMatrix, cases)

if __name__ == '__main__':
    pass
