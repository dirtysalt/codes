#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            from sortedcontainers import SortedList
            sl = SortedList()
            sl.add((nums[i], i))
            c = 0

            for j in range(i + 1, n):
                t = (nums[j], j)
                sl.add(t)
                pos = sl.index(t)

                if (pos + 1) < len(sl) and (pos - 1) >= 0:
                    a, _ = sl[pos - 1]
                    b, _ = sl[pos + 1]
                    if b - a > 1:
                        c -= 1

                if (pos - 1) >= 0:
                    a, _ = sl[pos - 1]
                    if nums[j] - a > 1:
                        c += 1
                if (pos + 1) < len(sl):
                    a, _ = sl[pos + 1]
                    if a - nums[j] > 1:
                        c += 1

                ans += c
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 1, 4], 3),
    ([1, 3, 3, 3, 5], 8,)
]

aatest_helper.run_test_cases(Solution().sumImbalanceNumbers, cases)

if __name__ == '__main__':
    pass
