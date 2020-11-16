#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        from collections import Counter
        cnt = Counter(nums)
        values = list(cnt.values())
        values.sort()
        quantity.sort()

        values = [x for x in values if x >= quantity[0]]
        if not values:
            return False
        if values[-1] < quantity[-1]:
            return False

        n, m = len(values), len(quantity)
        import functools
        @functools.lru_cache(maxsize=None)
        def match(i, xs):
            if i == m: return True
            for j in range(n):
                if xs[j] >= quantity[i]:
                    ys = list(xs)
                    ys[j] -= quantity[i]
                    ys = tuple(ys)
                    if match(i + 1, ys):
                        return True
            return False

        ans = match(0, tuple(values))
        return ans


cases = [
    ([1, 2, 3, 4], [2], False),
    ([1, 2, 3, 3], [2], True),
    ([1, 1, 1, 1, 1], [2, 3], True),
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17,
      17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31,
      31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45,
      45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50],
     [2, 2, 2, 2, 2, 2, 2, 2, 2, 3], False),
    ([1, 1, 1, 1, 2, 2, 2], [3, 2, 2], True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canDistribute, cases)
