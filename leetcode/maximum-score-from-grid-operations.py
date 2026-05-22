#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        import functools
        @functools.cache
        def dfs(j, pp, p):
            if j == m:
                res = 0
                for i in range(p + 1, pp + 1):
                    res += grid[i][j - 1]
                return res

            ans = 0
            for i in range(-1, n):
                res = 0
                for i2 in range(p + 1, max(pp, i) + 1):
                    res += grid[i2][j - 1]
                res += dfs(j + 1, p, i)
                ans = max(ans, res)
            return ans

        ans = 0
        for i in range(-1, n):
            r = dfs(1, -1, i)
            ans = max(ans, r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[5, 1, 3]], 8),
    ([[0, 0, 3], [0, 1, 0], [5, 0, 0]], 8),
    ([[0, 0, 3, 0], [0, 1, 0, 0], [5, 0, 0, 3]], 8),
    ([[0, 0, 3, 0, 0], [0, 1, 0, 0, 0], [5, 0, 0, 3, 0]], 11),
    ([[0, 0, 3, 0, 0], [0, 1, 0, 0, 0], [5, 0, 0, 3, 0], [0, 0, 0, 0, 2]], 11),
    ([[0, 0, 0, 0, 0], [0, 0, 3, 0, 0], [0, 1, 0, 0, 0], [5, 0, 0, 3, 0], [0, 0, 0, 0, 2]], 11),
    ([[10, 9, 0, 0, 15], [7, 1, 0, 8, 0], [5, 20, 0, 11, 0], [0, 0, 0, 1, 2], [8, 12, 1, 10, 3]], 94),
]

cases += aatest_helper.read_cases_from_file('tmp.in', 2)

aatest_helper.run_test_cases(Solution().maximumScore, cases)

if __name__ == '__main__':
    pass
