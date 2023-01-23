#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import queue


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        adj = []
        for _ in range(n):
            adj.append([])
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = queue.Queue()
        visited = [0] * n
        q.put((0, -1))
        while not q.empty():
            (v, src) = q.get()
            visited[v] = 1
            for to in adj[v]:
                if to == src:
                    continue
                if visited[to]:
                    return False
                visited[to] = 1
                q.put((to, v))
        return sum(visited) == n
