#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(i, c):
            color[i] = c
            for j in graph[i]:
                if color[j] == -1:
                    if not dfs(j, 1 - c):
                        return False
                elif color[j] != 1 - c:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
