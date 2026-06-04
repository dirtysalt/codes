#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        n = len(graph)
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for u in range(n):
            for w in graph[u]:
                adj[w].append(u)
                ind[u] += 1

        starts = []
        for u in range(n):
            if ind[u] == 0:
                starts.append(u)

        ans = []
        while starts:
            u = starts.pop()
            ans.append(u)
            for w in adj[u]:
                ind[w] -= 1
                if ind[w] == 0:
                    starts.append(w)
        ans.sort()
        return ans
