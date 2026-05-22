#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        @functools.cache
        def dfs(x, p):
            res = values[x]
            for y in adj[x]:
                if y == p: continue
                res += dfs(y, x)
            return res

        def best(x, p):
            if len(adj[x]) == 1 and adj[x][0] == p:
                # for leaf, we can not use it.
                return 0

            # use x
            a = values[x]
            for y in adj[x]:
                if y == p: continue
                a += best(y, x)

            # not use x
            b = dfs(x, p) - values[x]
            return max(a, b)

        ans = best(0, -1)
        return ans


if __name__ == '__main__':
    pass
