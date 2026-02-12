#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # 2^14 * 14 * 14 operations.

        n = len(nums)
        dp = [0] * (1 << n)

        def gcd(x, y):
            while y != 0:
                x, y = y, x %y
            return x

        for st in range(1 << n):
            bits = []
            for i in range(n):
                if st & (1 << i) == 0:
                    bits.append(i)

            if len(bits) % 2 != 0: continue
            w = 1 + (n - len(bits)) // 2

            for i in range(len(bits)):
                for j in range(i+1, len(bits)):
                    x = bits[i]
                    y = bits[j]
                    g = gcd(nums[x], nums[y])
                    wg = w * g
                    st2 = st | (1 << x) | (1 << y)
                    dp[st2] = max(dp[st2], dp[st] + wg)


        return dp[-1]

cases = [
    ([1,2], 1),
    ([3,4,6,8], 11),
    ([1,2,3,4,5,6], 14),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maxScore, cases)



if __name__ == '__main__':
    pass
