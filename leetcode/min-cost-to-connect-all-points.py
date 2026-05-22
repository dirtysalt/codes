#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        fu = [-1] * n

        def parent(x):
            p = x
            while fu[p] != -1:
                p = fu[p]
            while x != p:
                x2 = fu[x]
                fu[x] = p
                x = x2
            return p

        def merge(px, py):
            fu[px] = py

        ds = []
        for i in range(n):
            for j in range(i + 1, n):
                x, y = points[i]
                x2, y2 = points[j]
                d = abs(x - x2) + abs(y - y2)
                ds.append((d, i, j))
        ds.sort()
        ans = 0
        used = 0
        for d, i, j in ds:
            pi = parent(i)
            pj = parent(j)
            if pi != pj:
                merge(pi, pj)
                used += 1
                ans += d
                if used == (n - 1):
                    break
        return ans


cases = [
    ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
    ([[3, 12], [-2, 5], [-4, 1]], 18),
    ([[0, 0], [1, 1], [1, 0], [-1, 1]], 4),
    ([[-1000000, -1000000], [1000000, 1000000]], 4000000),
    ([[0, 0]], 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCostConnectPoints, cases)
