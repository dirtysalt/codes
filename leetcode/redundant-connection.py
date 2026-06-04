#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        N = len(edges)
        adj = [[] for _ in range(N)]
        for idx, (u, v) in enumerate(edges):
            u -= 1
            v -= 1
            adj[u].append((v, idx))
            adj[v].append((u, idx))

        def dfs(u, visited, remove_idx):
            visited[u] = 1
            for v, idx in adj[u]:
                if idx == remove_idx or visited[v]:
                    continue
                dfs(v, visited, remove_idx)

        ans = -1
        for remove_idx in range(N - 1, -1, -1):
            visited = [0] * N
            dfs(0, visited, remove_idx)
            if sum(visited) == N:
                ans = remove_idx
                break
        return edges[ans]
