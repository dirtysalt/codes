#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])

        def sim(x):
            for i in range(n):
                if grid[i][x] == 1:
                    if (x + 1) == m or grid[i][x + 1] == -1:
                        return -1
                    x = x + 1
                else:
                    if (x - 1) == -1 or grid[i][x - 1] == 1:
                        return -1
                    x = x - 1
            return x

        ans = []
        for x in range(m):
            p = sim(x)
            ans.append(p)
        return ans


cases = [
    ([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]],
     [1, -1, -1, -1, -1]),
    ([[-1]], [-1])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findBall, cases)
