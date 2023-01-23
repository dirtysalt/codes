#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        weight = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                w = n - j
                weight[i][preferences[i][j]] = w

        def isBad(x, y, u, v):
            w0 = weight[x][u]
            w1 = weight[x][y]
            w2 = weight[u][x]
            w3 = weight[u][v]
            return w0 > w1 and w2 > w3

        m = len(pairs)
        ss = set()
        ans = 0
        for i in range(m):
            bad = False
            for j in range(m):
                if i == j: continue
                x, y = pairs[i]
                u, v = pairs[j]
                if isBad(x, y, u, v) or isBad(x, y, v, u):
                    ss.add(x)
                if isBad(y, x, u, v) or isBad(y, x, v, u):
                    ss.add(y)
                if isBad(u, v, x, y) or isBad(u, v, y, x):
                    ss.add(u)
                if isBad(v, u, x, y) or isBad(v, u, y, x):
                    ss.add(v)
        ans = len(ss)
        return ans


cases = [
    (4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]], 2),
    (2, [[1], [0]], [[1, 0]], 0),
    (4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]], 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().unhappyFriends, cases)
