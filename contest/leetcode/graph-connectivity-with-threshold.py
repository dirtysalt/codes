#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        P = [-1] * (n + 1)

        def union(x, y):
            px = parent(x)
            py = parent(y)
            if px == py: return
            P[px] = py

        def parent(x):
            p = x
            while P[p] != -1:
                p = P[p]

            while x != p:
                x2 = P[x]
                P[x] = p
                x = x2
            return p

        ans = []
        if threshold == 0:
            ans.extend([True] * len(queries))
            return ans

        for x in range(threshold + 1, n + 1):
            for y in range(2, n // x + 1):
                union(x, x * y)

        for x, y in queries:
            px = parent(x)
            py = parent(y)
            ans.append(px == py)
        return ans


false = False
true = True

cases = [
    (6, 2, [[1, 4], [2, 5], [3, 6]], [false, false, true]),
    (6, 0, [[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]], [True, True, True, True, True]),
    (5, 1, [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]], [false, false, false, false, false]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().areConnected, cases)
