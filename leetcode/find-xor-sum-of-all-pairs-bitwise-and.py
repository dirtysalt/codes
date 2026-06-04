#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        maxv = max(max(arr1), max(arr2))
        maxbits = 0
        for i in reversed(range(32)):
            if maxv & (1 << i):
                maxbits = i + 1
                break

        def count(arr):
            ones = [0] * 32
            for i in range(maxbits):
                mask = 1 << i
                for x in arr:
                    if x & mask:
                        ones[i] += 1
            return ones

        a = count(arr1)
        b = count(arr2)
        ans = 0
        for i in range(32):
            c = a[i] * b[i]
            if c % 2:
                ans = ans | (1 << i)
        return ans

cases = [
    ([1,2,3], [6,5], 0),
    ([12], [4], 4),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().getXORSum, cases)




if __name__ == '__main__':
    pass
