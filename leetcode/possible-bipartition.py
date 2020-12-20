#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        visited = [0] * (N + 1)
        adj = [[] for _ in range(N + 1)]
        for (a, b) in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, c):
            visited[i] = c
            for j in adj[i]:
                if visited[j] and visited[j] != (3 - c):
                    return False
                if not visited[j]:
                    dfs(j, 3 - c)
            return True

        for i in range(1, N + 1):
            if not visited[i]:
                if not dfs(i, 1):
                    return False
        return True
