#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        n = len(nums)
        C = [0] * (n + k)

        c = 0
        for i in range(n):
            c -= C[i]
            v = nums[i] - c
            if v < 0: return False
            C[i + k] = v
            c += v

        if sum(C[-(k - 1):]) != 0: return False
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    ([0, 45, 82, 98, 99], 4, false),
    ([60, 72, 87, 89, 63, 52, 64, 62, 31, 37, 57, 83, 98, 94, 92, 77, 94, 91, 87, 100, 91, 91, 50, 26], 4, true),
    ([63, 40, 30, 0, 72, 53], 1, true),
]

aatest_helper.run_test_cases(Solution().checkArray, cases)

if __name__ == '__main__':
    pass
