#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        maxCoin = max(coins)

        @functools.cache
        def dfs(x, p, dep):
            if (1 << dep) > maxCoin:
                return 0

            a = coins[x] >> dep
            a -= k
            for y in adj[x]:
                if y == p: continue
                a += dfs(y, x, dep)

            b = coins[x] >> (dep + 1)
            for y in adj[x]:
                if y == p: continue
                b += dfs(y, x, dep + 1)

            return max(a, b)

        return dfs(0, -1, 0)


if __name__ == '__main__':
    pass
