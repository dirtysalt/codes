#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        import functools
        @functools.cache
        def find(r, c):
            a, b = 0, 0
            if r == 0 and c == 0:
                pass
            elif r == 0:
                a, b = find(r, c - 1)
            elif c == 0:
                a, b = find(r - 1, c)
            else:
                a0, b0 = find(r - 1, c)
                a1, b1 = find(r, c - 1)
                a2, b2 = find(r - 1, c - 1)
                a, b = a0 + a1 - a2, b0 + b1 - b2
            a += (grid[r][c] == 'X')
            b += (grid[r][c] == 'Y')
            return a, b

        n, m = len(grid), len(grid[0])
        ans = 0
        for r in range(n):
            for c in range(m):
                a, b = find(r, c)
                if a > 0 and a == b:
                    ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([["X", "Y", "."], ["Y", ".", "."]], 3),
    ([["X", "X"], ["X", "Y"]], 0),
    ([[".", "."], [".", "."]], 0),
]

aatest_helper.run_test_cases(Solution().numberOfSubmatrices, cases)

if __name__ == '__main__':
    pass
