#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import OrderedDict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(x, p):
            res = 0
            c = values[x] % k
            for y in adj[x]:
                if y == p: continue
                c2, r2 = dfs(y, x)
                c = (c + c2) % k
                res += r2
            if c == 0:
                res += 1
            return c, res

        _, ans = dfs(0, -1)
        # for i in range(0, n):
        #     assert (dfs(i, -1)[1] == ans)
        # return ans
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    OrderedDict(n=5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6, res=2),
    OrderedDict(n=7, edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[3, 0, 6, 1, 5, 2, 1], k=3, res=3),
    (1, [], [10000], 100, 1)
]

aatest_helper.run_test_cases(Solution().maxKDivisibleComponents, cases)

if __name__ == '__main__':
    pass
