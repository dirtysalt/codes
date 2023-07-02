#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()
        n = len(nums)

        ans = 0
        j = 0
        for i in range(n):
            sl.add(nums[i])
            while sl[-1] - sl[0] > 2:
                sl.remove(nums[j])
                j += 1
            # [j .. i] works
            # [(j..i), i] works
            ans += i - j + 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 4, 2, 4], 8),
    ([1, 2, 3], 6),
]

aatest_helper.run_test_cases(Solution().continuousSubarrays, cases)

if __name__ == '__main__':
    pass
