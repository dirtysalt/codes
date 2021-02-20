#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import aatest_helper
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = max(min(a[0], a[1]) for a in rectangles)
        ans = 0
        for a, b in rectangles:
            if a >= maxLen and b >= maxLen:
                ans += 1
        return ans


cases = [
    ([[5, 8], [3, 9], [5, 12], [16, 5]], 3),
    ([[2, 3], [3, 7], [4, 3], [3, 7]], 3)
]

aatest_helper.run_test_cases(Solution().countGoodRectangles, cases)
