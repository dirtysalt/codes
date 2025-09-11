#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for f, t, c in edges:
            self.adj[f].append((t, c))

    def addEdge(self, edge: List[int]) -> None:
        f, t, c = edge
        self.adj[f].append((t, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        import heapq
        INF = 1 << 30
        hp, adj, dist = [], self.adj, [INF] * self.n
        hp.append((0, node1))
        # print(dist)
        while hp:
            (d, x) = heapq.heappop(hp)
            if x == node2: return d
            dist[x] = d
            for y, c in adj[x]:
                c = c + d
                if dist[y] > c:
                    dist[y] = c
                    heapq.heappush(hp, (c, y))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

if __name__ == '__main__':
    pass
