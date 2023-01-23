#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        from collections import Counter
        total = [0] * k
        dist = [Counter() for _ in range(k)]
        n = len(nums)
        for i in range(n):
            x = nums[i]
            dist[i % k][x] += 1
            total[i % k] += 1

        inf = 1 << 20
        import array
        # dp = [[0] * 1024 for _ in range(2)]
        dp = [array.array('I', [0] * 1024) for _ in range(2)]
        for i in range(1024):
            dp[0][i] = inf
        dp[0][0] = 0

        now = 0
        for i in range(k):
            dp0 = dp[now]
            dp1 = dp[1-now]
            base = min(dp0) + total[i]
            for x in range(1024):
                dp1[x] = base
            for x in range(1024):
                for k, c in dist[i].items():
                    dp1[x^k] = min(dp1[x^k], total[i] - c + dp0[x])
            now = 1-now

        return dp[now][0]

cases = [
    ([1,2,0,3,0], 1,3),
    ( [3,4,5,2,1,7,3,4,7], 3,3),
    ( [1,2,4,1,2,5,1,2,6], 3,3),
    ([26,19,19,28,13,14,6,25,28,19,0,15,25,11],3,11),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minChanges, cases)


if __name__ == '__main__':
    pass
