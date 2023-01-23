#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [[0] * (1 + k) for _ in range(n + 1)]
        dp[0][0] = 1

        # dp[i][j] 前面i个木棍可以看到j根
        # 如果可以看到ith的话，那么数量为dp[i-1][j-1]
        # 如果看不到ith的话（不是这根棍子，而是这个位置上的木棍），那么取前面(i-1)里面任意一个出来放在ith的最后，
        # 接下来就是从前面i个目录里面看到j根，所以结果是 (i-1)* dp[i-1][j]
        for k2 in range(1, k + 1):
            for i in range(1, n + 1):
                dp[i][k2] = dp[i - 1][k2 - 1] + (i - 1) * dp[i - 1][k2]

        ans = dp[n][k]
        MOD = 10 ** 9 + 7
        return ans % MOD


import aatest_helper

cases = [
    (3, 2, 3),
    (5, 5, 1),
    (20, 11, 647427950),
    # (1000, 1000, aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().rearrangeSticks, cases)

if __name__ == '__main__':
    pass
