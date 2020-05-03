#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """

    def findMinHeightTrees(self, n, edges):
        # Wirte your code here

        if n == 1: return [0]
        adj = [[] for x in range(n)]
        deg = [0] * n
        for (u, v) in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1

        leaves = [v for v in range(n) if deg[v] == 1]
        depths = [0] * n
        to_visits = []
        for leaf in leaves:
            to_visits.append((leaf, 1))
            depths[leaf] = 1

        nodes = n
        while nodes > 2:
            next_visits = []
            for (v, d) in to_visits:
                d2 = d + 1
                for v2 in adj[v]:
                    deg[v2] -= 1
                    if deg[v2] in (0, 1) and not depths[v2]:
                        depths[v2] = d2
                        next_visits.append((v2, d2))
            nodes -= len(to_visits)
            to_visits = next_visits

        res = [x[0] for x in to_visits]
        return res
