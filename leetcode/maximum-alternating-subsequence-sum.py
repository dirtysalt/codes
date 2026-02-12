#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        i = 0
        nums.append(0)
        n = len(nums)

        res = 0
        while i < n:
            # find largest one.
            j = i + 1
            while j < n and nums[j] >= nums[j - 1]: j += 1
            a = nums[j - 1]

            # find smallest one.
            while j < n and nums[j] <= nums[j - 1]: j += 1
            b = nums[j - 1]
            i = j

            res += (a - b)
        return res


true, false, null = True, False, None
cases = [
    ([4, 2, 5, 3], 7),
    ([5, 6, 7, 8], 8),
    ([6, 2, 1, 2, 4, 5], 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxAlternatingSum, cases)

if __name__ == '__main__':
    pass
