#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isCompliance(self, distance: List[List[int]], n: int) -> bool:
        N = len(distance)
        adj = [set() for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if distance[i][j] <= 2:
                    adj[i].add(j)
                    adj[j].add(i)

        mask = set()

        def dfs(x):
            mask.add(x)
            for y in adj[x]:
                if y not in mask:
                    dfs(y)

        t = 0
        for i in range(N):
            if i in mask: continue
            t += 1
            dfs(i)
        return t <= n


true, false, null = True, False, None
cases = [
    ([[0, 1, 3], [1, 0, 3], [3, 3, 0]], 2, true),
    ([[0, 3, 3], [3, 0, 3], [3, 3, 0]], 2, false),
    ([[0, 3, 1, 4], [3, 0, 1, 3], [1, 1, 0, 5], [4, 3, 5, 0]], 2, true)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isCompliance, cases)

if __name__ == '__main__':
    pass
