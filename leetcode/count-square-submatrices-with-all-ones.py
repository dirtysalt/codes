#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    continue
                a = dp[i - 1][j - 1] if (i >= 1 and j >= 1) else 0
                b = dp[i - 1][j] if (i >= 1) else 0
                c = dp[i][j - 1] if (j >= 1) else 0
                sz = min(a, b, c)
                dp[i][j] = sz + 1
                ans += sz + 1
        return ans


cases = [
    ([
         [0, 1, 1, 1],
         [1, 1, 1, 1],
         [0, 1, 1, 1]
     ], 15)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSquares, cases)
