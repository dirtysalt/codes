#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 好巧妙的方法，这里还提供了一种dfs遍历tree的方式，只需要保存parent即可
# Discuss里面有个Java版本的 graph memorization实现也很有意思. 为不同方向的边保存了不同的 num 和 sum.

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * N
        count = [0] * N

        def dfs1(x, parent):
            dist = 0
            cnt = 1
            for y in adj[x]:
                if y == parent: continue
                dfs1(y, x)
                dist += ans[y] + count[y]
                cnt += count[y]
            ans[x] = dist
            count[x] = cnt

        def dfs2(x, parent):
            for y in adj[x]:
                if y == parent: continue
                ans[y] += ans[x] - (count[y] + ans[y]) + (N - count[y])
                dfs2(y, x)

        dfs1(0, -1)
        dfs2(0, -1)
        return ans
