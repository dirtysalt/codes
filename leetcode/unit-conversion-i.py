#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        n = len(conversions) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in conversions:
            adj[u].append((v, w))

        MOD = 10 ** 9 + 7
        ans = [1] * n

        def dfs(r):
            for v, w in adj[r]:
                ans[v] = (ans[r] * w) % MOD
                dfs(v)

        dfs(0)
        return ans


if __name__ == '__main__':
    pass
