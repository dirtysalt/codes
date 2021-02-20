#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        inf = 1 << 30
        dp = [inf] * (n + 1)

        for i in range(n + 1):
            r = ranges[i]
            if r == 0:
                continue
            y = i - r
            base = dp[y] if y > 0 else 0
            for x in range(max(0, i - r + 1), min(i + r + 1, n + 1)):
                dp[x] = min(dp[x], base + 1)

        ans = dp[n]
        if ans == inf:
            ans = -1
        return ans


cases = [
    (35, [1, 0, 4, 0, 4, 1, 4, 3, 1, 1, 1, 2, 1, 4, 0, 3, 0, 3, 0, 3, 0, 5, 3, 0, 0, 1, 2, 1, 2, 4, 3, 0, 1, 0, 5, 2],
     6),

    (5, [3, 4, 1, 1, 0, 0], 1),
    (8, [4, 0, 0, 0, 4, 0, 0, 0, 4], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minTaps, cases)
