#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(x, y, z):
            # (1/2)*[(x2y3-x3y2)-(x1y3-x3y1)+(x1y2-x2y1)]
            x1, y1 = x
            x2, y2 = y
            x3, y3 = z
            return abs(0.5 * ((x2 * y3 - x3 * y2) - (x1 * y3 - x3 * y1) + (x1 * y2 - x2 * y1)))

        n = len(points)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = area(points[i], points[j], points[k])
                    ans = max(ans, a)
        return ans
