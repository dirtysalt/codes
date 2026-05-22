#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        ans = 0
        for i in range(n - 1):
            d = heights[i + 1] - heights[i]
            if d <= 0:
                ans = i + 1
                continue

            if d <= bricks:
                bricks -= d
                ans = i + 1
                continue

            if ladders:
                ladders -= 1
                ans = i + 1
                continue

            break
        return ans


cases = [
    ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
    ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
    ([14, 3, 19, 3], 17, 0, 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().furthestBuilding, cases)
