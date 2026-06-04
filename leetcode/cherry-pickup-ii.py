#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = {}
        n = len(grid)
        m = len(grid[0])

        def fun(r, x, y):
            if r == n:
                return 0
            key = (r, x, y)
            if key in dp:
                return dp[key]

            if x != y:
                val = grid[r][x] + grid[r][y]
            else:
                val = grid[r][x]
            res = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < m and 0 <= y + dy < m:
                        res = max(fun(r + 1, x + dx, y + dy), res)
            ans = res + val
            dp[key] = ans
            return ans

        ans = fun(0, 0, m - 1)
        return ans


cases = [
    ([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]], 24),
    ([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]], 22),
    ([[1, 1], [1, 1]], 4)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().cherryPickup, cases)
