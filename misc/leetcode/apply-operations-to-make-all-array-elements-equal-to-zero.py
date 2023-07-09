#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        nums.extend([0] * k)
        n = len(nums)
        C = [0] * (n + k)

        c = 0
        for i in range(n):
            c -= C[i]
            v = nums[i] - c
            if v < 0: return False
            C[i + k] = v
            c += v
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 2, 3, 1, 1, 0], 3, true),
    ([1, 3, 1, 1], 2, false),
    ([0, 45, 82, 98, 99], 4, false)
]

aatest_helper.run_test_cases(Solution().checkArray, cases)

if __name__ == '__main__':
    pass
