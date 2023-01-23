#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = 0, 0, 0
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                # print(x, y, z)
                a = max(a, x)
                b = max(b, y)
                c = max(c, z)
        return (a, b, c) == tuple(target)


true, false, null = True, False, None
cases = [
    ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], true),
    ([[1, 3, 4], [2, 5, 8]], [2, 5, 8], true),
    ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], true),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().mergeTriplets, cases)

if __name__ == '__main__':
    pass
