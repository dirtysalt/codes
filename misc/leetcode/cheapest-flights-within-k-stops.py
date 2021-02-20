#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        inf = 1 << 20
        dist = [[inf] * n for _ in range(n)]
        mat = [[[inf] * n for _ in range(n)],
               [[inf] * n for _ in range(n)]]
        for (f, t, c) in flights:
            dist[f][t] = c
            mat[0][f][t] = c

        now = 0
        for _ in range(K):
            for t in range(n):
                mat[1 - now][src][t] = min(mat[1 - now][src][t], mat[now][src][t])
                for v in range(n):
                    mat[1 - now][src][t] = min(mat[now][src][v] + dist[v][t], mat[1 - now][src][t])
            now = 1 - now

        ans = mat[now][src][dst]
        if ans == inf:
            ans = -1
        return ans


cases = [
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
    (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1, 6),
    (3, [[0, 1, 2], [1, 2, 1], [2, 0, 10]], 1, 2, 1, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findCheapestPrice, cases)
