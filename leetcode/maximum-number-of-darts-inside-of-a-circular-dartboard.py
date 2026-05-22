#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def find_center(x1, y1, x2, y2, r):
            dx, dy = x2 - x1, y2 - y1
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            d2 = (mx - x1) ** 2 + (my - y1) ** 2
            rd = (r * r - d2) ** 0.5
            dxy = (dx ** 2 + dy ** 2) ** 0.5
            x3 = -dy * rd / dxy + mx
            y3 = dx * rd / dxy + my
            return x3, y3

        ans = 1
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                if i == j: continue
                if (x2 - x1) ** 2 + (y2 - y1) ** 2 > 4 * r * r: continue
                x3, y3 = find_center(x1, y1, x2, y2, r)
                res = 0
                for k in range(n):
                    if k == i or k == j:
                        res += 1
                        continue

                    x4, y4 = points[k]
                    if (x3 - x4) ** 2 + (y3 - y4) ** 2 <= r * r:
                        res += 1
                ans = max(ans, res)
        return ans


cases = [
    ([[-2, 0], [2, 0], [0, 2], [0, -2]], 2, 4),
    ([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5, 5),
    ([[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], 2, 4),
    ([[-2, 0], [2, 0], [0, 2], [0, -2]], 1, 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numPoints, cases)
