#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        back = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            back[y].append(x)

        import functools
        @functools.cache
        def dfs_out(u, p):
            res = 0
            for v in back[u]:
                if v == p: continue
                res += 1
                res += dfs_out(v, u)

            for v in adj[u]:
                if v == p: continue
                res += dfs_out(v, u)
            return res

        ans = [0] * n
        for i in range(n):
            ans[i] = dfs_out(i, -1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, [[2, 0], [2, 1], [1, 3]], [1, 1, 0, 2]),
    (3, [[1, 2], [2, 0]], [2, 0, 1]),
]

aatest_helper.run_test_cases(Solution().minEdgeReversals, cases)

if __name__ == '__main__':
    pass
