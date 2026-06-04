#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList(nums)
        ans = 0
        for x in nums:
            sl.remove(x)
            a, b = lower - x, upper - x
            i = sl.bisect_left(a)
            j = sl.bisect_right(b)
            ans += (j - i)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([0, 1, 7, 4, 4, 5], 3, 6, 6),
    ([1, 7, 9, 2, 5], 11, 11, 1),
]

aatest_helper.run_test_cases(Solution().countFairPairs, cases)

if __name__ == '__main__':
    pass
