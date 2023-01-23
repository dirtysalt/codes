#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findRedundantDirectedConnection(self, edges):
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

        def dfs(u, visited, remove_idx):
            visited[u] = 1
            for v, idx in adj[u]:
                if idx == remove_idx or visited[v]:
                    continue
                dfs(v, visited, remove_idx)

        ans = -1
        for remove_idx in range(N - 1, -1, -1):
            ind = [0] * N
            for u in range(N):
                for v, idx in adj[u]:
                    if idx == remove_idx: continue
                    ind[v] += 1

            src = None
            ok = True
            for u in range(N):
                if ind[u] != 0: continue
                if src is not None:
                    ok = False
                    break
                src = u
            if not ok:
                continue

            visited = [0] * N
            dfs(src, visited, remove_idx)
            if sum(visited) == N:
                ans = remove_idx
                break
        return edges[ans]
