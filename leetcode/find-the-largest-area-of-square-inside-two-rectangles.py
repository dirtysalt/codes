#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        rects = list(zip(bottomLeft, topRight))
        n = len(rects)

        def overlap(i, j):
            (x0, y0), (x1, y1) = rects[i]
            (x2, y2), (x3, y3) = rects[j]
            if x0 > x2:
                (x0, x1, x2, x3) = (x2, x3, x0, x1)
            if x1 <= x2: return 0
            xsz = min(x1, x3) - x2

            if y0 > y2:
                (y0, y1, y2, y3) = (y2, y3, y0, y1)
            if y1 <= y2: return 0
            ysz = min(y1, y3) - y2

            return min(xsz, ysz) ** 2

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                r = overlap(i, j)
                ans = max(ans, r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]], 1),
    ([[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]], 1),
    ([[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]], 0),
]

aatest_helper.run_test_cases(Solution().largestSquareArea, cases)

if __name__ == '__main__':
    pass
