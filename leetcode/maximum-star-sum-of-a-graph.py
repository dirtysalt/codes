#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        ans = -(1 << 30)
        for i in range(n):
            adj[i].sort(key=lambda x: -vals[x])
            res = vals[i] + sum((vals[x] for x in adj[i][:k] if vals[x] > 0))
            ans = max(ans, res)
        return ans


if __name__ == '__main__':
    pass
