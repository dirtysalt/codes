#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        N = min(10 ** 5, max(nums))
        occ = [0] * (1 + N)
        for x in nums:
            occ[x] += 1
        acc = [0] * (2 + N)
        for i in range(1, N + 1):
            acc[i + 1] = occ[i]
            acc[i + 1] += acc[i]

        ans = 0
        for x in range(1, 1 + N):
            if occ[x] == 0: continue
            m = 1
            while True:
                t = m * x
                if t > N: break
                s, e = t, min(t + x - 1, N)
                tt = acc[e + 1] - acc[s]
                # if tt:
                #     print(x, m, s, e, tt)
                ans += tt * occ[x] * m
                m += 1

        MOD = 10 ** 9 + 7
        return ans % MOD


cases = [
    ([2, 5, 9], 10),
    ([7, 7, 7, 7, 7, 7, 7], 49)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumOfFlooredPairs, cases)
