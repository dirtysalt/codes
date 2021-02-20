#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] += acc[i] + stones[i]

        #         dp = {}
        #         def test(i, j):
        #             if i > j: return 0
        #             key = (i, j)
        #             if key in dp: return dp[key]
        #             tt = acc[j+1] - acc[i]
        #             a = tt - stones[i]
        #             aa = test(i+1, j)
        #             b = tt - stones[j]
        #             bb = test(i, j-1)
        #             ans = max(a - aa, b - bb)
        #             dp[key] = ans
        #             return ans

        #         ans = test(0, n-1)

        dp = [[0] * n, [0] * n]
        cur = 0
        for sz in range(2, n + 1):
            for i in range(n - sz + 1):
                # stones[i..i+sz-1]
                j = i + sz - 1
                tt = acc[j + 1] - acc[i]
                a = tt - stones[i]
                aa = dp[cur][i + 1]
                b = tt - stones[j]
                bb = dp[cur][i]
                dp[1 - cur][i] = max(a - aa, b - bb)
            cur = 1 - cur

        ans = dp[cur][0]
        return ans


cases = [
    ([5, 3, 1, 4, 2], 6),
    ([7, 90, 5, 1, 100, 10, 10, 2], 122)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().stoneGameVII, cases)
