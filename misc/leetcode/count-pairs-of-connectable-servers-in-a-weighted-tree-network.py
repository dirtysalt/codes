#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for x, y, d in edges:
            adj[x].append((y, d))
            adj[y].append((x, d))

        def test(x):
            def dfs(i, d, p):
                res = 0
                if d % signalSpeed == 0:
                    res += 1
                for j, d2 in adj[i]:
                    if j == p: continue
                    res += dfs(j, d + d2, i)
                return res

            rs = []
            for y, d in adj[x]:
                r = dfs(y, d, x)
                rs.append(r)
            acc = sum(rs)
            ans = 0
            for r in rs:
                ans += r * (acc - r)
            return ans // 2

        ans = [0] * n
        for x in range(n):
            ans[x] = test(x)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(edges=[[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], signalSpeed=1,
                              res=[0, 4, 6, 6, 4, 0]),
    aatest_helper.OrderedDict(edges=[[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], signalSpeed=3,
                              res=[2, 0, 0, 0, 0, 0, 2]),
    ([[1, 0, 2], [2, 1, 4], [3, 2, 4], [4, 0, 3], [5, 1, 4], [6, 2, 2], [7, 6, 4], [8, 1, 2], [9, 8, 3]], 1,
     [8, 28, 20, 0, 0, 0, 8, 0, 8, 0]),
]

aatest_helper.run_test_cases(Solution().countPairsOfConnectableServers, cases)

if __name__ == '__main__':
    pass
