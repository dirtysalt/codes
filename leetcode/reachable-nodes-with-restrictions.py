#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        r = set(restricted)

        def dfs(x):
            c = 1
            r.add(x)
            for y in adj[x]:
                if y in r: continue
                c += dfs(y)
            return c

        ans = dfs(0)
        return ans


if __name__ == '__main__':
    pass
