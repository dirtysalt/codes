#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def fraction(self, cont: List[int]) -> List[int]:

        def add(x, y, a, b):
            if a == 0: return x, y
            if x == 0: return a, b
            t0, t1 = x * b + y * a, y * b
            g = gcd(t0, t1)
            return t0 // g, t1 // g

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x


        t0, t1 = 0, 0
        for v in cont[::-1]:
            t0, t1 = add(t1, t0, v, 1)

        return [t0, t1]

cases = [
    ([3, 2, 0, 2], [13,4]),
    ([0, 0, 3], [3,1]),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().fraction, cases)


if __name__ == '__main__':
    pass
