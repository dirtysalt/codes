#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0

        pts = [tuple(x) for x in points]
        pts.sort()

        end = pts[0][1]
        ans = 1
        for s, e in pts:
            if s <= end:
                end = min(end, e)
                continue
            ans += 1
            end = e
        return ans


cases = [
    ([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]], 2),
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findMinArrowShots, cases)
