#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        a = index
        b = n - index - 1

        def test(x):
            a0 = min(a, x-1)
            b0 = min(b, x-1)
            t0 = (a0 + 1) * a0 // 2 + (b0 + 1) *b0 // 2
            t1 = (n-a0-b0-1)
            tmin = (a0+b0+1) * x - t0 + t1
            return tmin <= maxSum

        s, e = 1, maxSum
        while s <= e:
            m = (s + e) // 2
            ok = test(m)
            if ok:
                s = m + 1
            else:
                e = m - 1
        ans = e
        return ans

cases = [
    ( 4, 2,6,2),
    (6,1,10,3),
    (3,2,18,7),
    (8,7,14,4),
    (4,0,4,1),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maxValue, cases)




if __name__ == '__main__':
    pass
