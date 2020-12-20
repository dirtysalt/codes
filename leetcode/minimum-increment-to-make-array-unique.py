#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A: return 0
        min_value, max_value = min(A), max(A)
        c = [0] * (max_value - min_value + 1)
        for x in A:
            c[x - min_value] += 1

        ans = 0
        p = 0
        for i in range(min_value, max_value + 1):
            idx = i - min_value
            p += c[idx]
            if p > 1:
                ans += (p - 1)
                p -= 1
            else:
                p = 0
        ans += p * (p - 1) // 2
        return ans


cases = [
    ([1, 2, 2], 1),
    ([3, 2, 1, 2, 1, 7], 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minIncrementForUnique, cases)
