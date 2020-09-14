#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [[] for _ in range(n)]

        for (x, y), prob in zip(edges, succProb):
            dist[x].append((y, prob))
            dist[y].append((x, prob))

        ans = [0] * n
        visited = [0] * n
        import heapq
        hp = []
        hp.append((-1, start))

        while hp:
            (prob, x) = heapq.heappop(hp)
            if visited[x]: continue
            ans[x] = -prob
            visited[x] = 1
            # if x == end: break
            for y, p in dist[x]:
                if visited[y]: continue
                heapq.heappush(hp, (prob * p, y))
        return ans[end]


cases = [
    (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProbability, cases)
