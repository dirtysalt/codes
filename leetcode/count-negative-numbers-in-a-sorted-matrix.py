#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        ans = 0
        p = 0
        for i in reversed(range(n)):
            while p < m and grid[i][p] >= 0:
                p += 1
            ans += m - p
        return ans


cases = [
    ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countNegatives, cases)
