#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        depth = [-1] * n
        from collections import deque
        adj = [[] for _ in range(n)]
        for (x, y) in edges:
            adj[x].append(y)
            adj[y].append(x)
        dq = deque()
        dq.append(0)
        depth[0] = 0

        while dq:
            x = dq.popleft()
            d = depth[x]
            for y in adj[x]:
                if depth[y] == -1:
                    depth[y] = d + 1
                    dq.append(y)

        cost = [0] * n
        xs = [(depth[i], i) for i in range(n)]
        xs.sort(reverse=True)
        has = hasApple.copy()
        print(depth, xs)
        for d, x in xs:
            if not has[x]: continue
            for y in adj[x]:
                if depth[y] == d - 1:
                    cost[y] += cost[x] + 2
                    has[y] = True
        ans = cost[0]
        return ans
