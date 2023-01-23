#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for (x, y) in edges:
            adj[x].append(y)
            adj[y].append(x)
            ind[x] += 1
            ind[y] += 1

        opts = []
        for i in range(n):
            if ind[i] in (0, 1):
                opts.append(i)
        left = n - len(opts)

        while left != 0:
            new_opts = []
            for x in opts:
                for y in adj[x]:
                    ind[y] -= 1
                    if ind[y] == 1:
                        new_opts.append(y)
                        left -= 1
            opts = new_opts
        ans = opts
        return ans


cases = [
    (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]], [3, 4]),
    (4, [[1, 0], [1, 2], [1, 3]], [1]),
    (1, [], [0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findMinHeightTrees, cases)
