#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pts = set()
        for x, y in points:
            pts.add((x, y))

        n = len(points)
        inf = 1 << 30
        ans = inf
        for i in range(n):
            x0, y0 = points[i]
            for j in range(i + 1, n):
                x1, y1 = points[j]
                if x1 == x0 or y1 == y0: continue
                if (x1, y0) in pts and (x0, y1) in pts:
                    area = (x1 - x0) * (y1 - y0)
                    area = abs(area)
                    ans = min(ans, area)
        if ans == inf:
            ans = 0
        return ans


cases = [
    ([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]], 4),
    ([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minAreaRect, cases)
