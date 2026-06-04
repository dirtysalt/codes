#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                v = matrix[i][j]
                if v == '0':
                    dp[i][j] = 0
                    continue

                dp[i][j] = 1
                if i > 0 and j > 0:
                    a = dp[i-1][j]
                    b = dp[i][j-1]
                    c = dp[i-1][j-1]
                    dp[i][j] = min(a, b, c) + 1
                ans = max(ans, dp[i][j])
        
        # for x in dp:
        #     print(x)
        return ans * ans


cases = [
    ([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
     "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]], 4)
]
import aatest_helper
aatest_helper.run_test_cases(Solution().maximalSquare, cases)
