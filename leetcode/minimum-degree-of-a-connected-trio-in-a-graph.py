#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        conn = [0] * n
        adj = [set() for _ in range(n)]
        for (x, y) in edges:
            x = x - 1
            y = y - 1
            adj[x].add(y)
            adj[y].add(x)
            conn[x] += 1
            conn[y] += 1

        ans = -1
        for s in range(n):
            for e in adj[s]:
                if e < s: continue
                for t in range(e + 1, n):
                    if t in adj[s] and t in adj[e]:
                        deg = conn[s] + conn[e] + conn[t] - 6
                        if ans == -1 or deg < ans:
                            ans = deg
        return ans


cases = [
    (6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]], 3),
    (7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minTrioDegree, cases)
