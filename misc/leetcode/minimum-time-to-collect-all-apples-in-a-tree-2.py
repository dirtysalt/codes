#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        visited = [0] * n
        adj = [[] for _ in range(n)]
        for (x, y) in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(x):
            visited[x] = 1
            cost = 0
            for y in adj[x]:
                if not visited[y]:
                    c = dfs(y)
                    if c >= 0:
                        cost += (c + 2)
            if cost == 0:
                if hasApple[x]:
                    return 0
                return -1
            return cost

        ans = dfs(0)
        if ans == -1:
            ans = 0
        return ans
