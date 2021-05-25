#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = stones[i] + acc[i]

        # 状态方程是dp[i]表示从i开始选择，alice-bob的最大差值
        # alice不选择ith的话，那么dp[i] = dp[i+1]
        # 如果选择ith的话，那么alice获得acc[i+1] value,
        # 接下来就是bob取，所以dp[i] = acc[i+1] - dp[i+1]

        dp = [0] * n
        dp[n - 1] = acc[n]
        # dp[i] = max(dp[i+1], acc[i+1] - dp[i+1])
        for i in reversed(range(1, n-1)):
            dp[i] = max(dp[i+1], acc[i+1] - dp[i+1])
        # have to take one stone.
        ans = dp[1]
        return ans


true, false, null = True, False, None
cases = [
    ([-1, 2, -3, 4, -5], 5),
    ([7, -6, 5, 10, 5, -2, -6], 13),
    ([-10, -12], -22),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().stoneGameVIII, cases)

if __name__ == '__main__':
    pass
