#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        def concat(a, b):
            v = a[0] / b[0]
            x = a[1]
            y = b[1]
            if b[2] > 1:
                y = '(' + y + ')'
            z = x + '/' + y
            return (v, z, a[2] + b[2])

        import functools
        functools.lru_cache(maxsize = None)
        def search(i, j):
            if i == j:
                x = (nums[i], '%s' % (nums[i]), 1)
                return (x, x)

            Min = None
            Max = None
            for k in range(i, j):
                lmin, lmax = search(i, k)
                rmin, rmax = search(k+1, j)
                print(lmin, rmax)
                x = lmin[0] / rmax[0]
                if Min is None or x < Min[0]:
                    Min = concat(lmin, rmax)
                x = lmax[0] / rmin[0]
                if Max is None or x > Max[0]:
                    Max = concat(lmax, rmin)

            return Min, Max

        a, b = search(0, len(nums) - 1)
        ans = b[1]
        return ans

cases = [
    ([1000,100,10,2], "1000/(100/10/2)"),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().optimalDivision, cases)


if __name__ == '__main__':
    pass
