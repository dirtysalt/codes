#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Graph:
    def __init__(self, n):
        self.n = n
        self.d = []
        for i in range(n):
            self.d.append([])

    def connect(self, s, e):
        self.d[s].append(e)
        self.d[e].append(s)

    def find_all_distances(self, s):
        dist = [-1] * self.n

        dist[s] = 0
        queue = [(s, 0)]
        queue_idx = 0

        while queue_idx < len(queue):
            (v, d) = queue[queue_idx]
            queue_idx += 1
            for v2 in self.d[v]:
                if dist[v2] != -1:
                    continue
                dist[v2] = d + 1
                queue.append((v2, d + 1))

        dist = [x * 6 if x > 0 else -1 for x in dist]
        dist.pop(s)
        print((' '.join(map(str, dist))))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    try:
        s = int(input())
    except Exception:
        s = 1
    graph.find_all_distances(s - 1)
