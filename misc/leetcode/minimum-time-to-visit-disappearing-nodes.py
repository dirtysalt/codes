#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        es = {}
        for u, v, w in edges:
            if u > v:
                u, v = v, u
            old = es.get((u, v), None)
            if old is None or old > w:
                es[(u, v)] = w

        adj = [[] for _ in range(n)]
        for (u, v), w in es.items():
            adj[u].append((v, w))
            adj[v].append((u, w))

        miss = [(i, t) for (i, t) in enumerate(disappear)]
        miss.sort(key=lambda x: x[1], reverse=True)

        INF = 1 << 30
        import heapq
        pq = []
        dist = [-1] * n
        pq.append((0, 0))

        while pq:
            (t, x) = heapq.heappop(pq)

            while miss and miss[-1][1] <= t:
                i, _ = miss.pop()
                if dist[i] == -1:
                    dist[i] = INF

            if dist[x] != -1: continue
            dist[x] = t
            for y, w in adj[x]:
                heapq.heappush(pq, (t + w, y))

        for i in range(n):
            if dist[i] == INF:
                dist[i] = -1
        return dist


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 1, 5], res=[0, -1, 4]),
    aatest_helper.OrderedDict(n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 3, 5], res=[0, 2, 3]),
    aatest_helper.OrderedDict(n=2, edges=[[0, 1, 1]], disappear=[1, 1], res=[0, -1]),
    aatest_helper.OrderedDict(n=9, edges=[[5, 1, 3], [8, 3, 4], [0, 3, 5], [6, 1, 4], [5, 3, 9]],
                              disapper=[4, 13, 13, 19, 13, 15, 15, 16, 16], res=[0, -1, -1, 5, -1, 14, -1, -1, 9]),
]

aatest_helper.run_test_cases(Solution().minimumTime, cases)

if __name__ == '__main__':
    pass
