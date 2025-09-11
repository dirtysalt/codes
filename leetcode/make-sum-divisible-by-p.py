#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p
        last = {}
        last[0] = -1

        t = 0
        ans = n
        for i in range(n):
            t += nums[i]
            t = t % p
            last[t] = i

            # t - x = target
            # x = (t - target)
            exp = (t - target + p) % p
            if exp in last:
                dist = i - last[exp]
                ans = min(ans, dist)

        if ans == n:
            ans = -1
        return ans

cases = [
    ([3,1,4,2],6,1),
    ([6,3,5,2], 9,2),
    ([1,2,3], 3, 0),
    ([1,2,3], 7, -1),
    ([1000000000,1000000000,1000000000], 3, 0),
    ([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2],148,7),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minSubarray, cases)


if __name__ == '__main__':
    pass
