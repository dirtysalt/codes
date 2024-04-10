#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        cut = [-1] * n
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dfs(x, c):
            cut[x] = c
            value = 0xffffffff
            for y, w in adj[x]:
                value &= w
                if cut[y] != -1: continue
                value &= dfs(y, c)
            return value

        c = 0
        values = []
        for i in range(n):
            if cut[i] != -1: continue
            value = dfs(i, c)
            values.append(value)
            c += 1

        ans = []
        for x, y in query:
            if cut[x] == cut[y]:
                ans.append(values[cut[x]])
            else:
                ans.append(-1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=5, edges=[[0, 1, 7], [1, 3, 7], [1, 2, 1]], query=[[0, 3], [3, 4]], res=[1, -1]),
    aatest_helper.OrderedDict(n=3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]], res=[0]),
]

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
