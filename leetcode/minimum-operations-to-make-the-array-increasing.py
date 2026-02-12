#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        x = nums[0]
        for i in range(1, len(nums)):
            y = nums[i]
            to = max(x + 1, y)
            ans += to - y
            x = to
        return ans
cases = [
    ([1,5,2,4,1], 14),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minOperations, cases)


if __name__ == '__main__':
    pass
