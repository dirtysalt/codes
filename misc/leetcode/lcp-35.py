#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        n = len(charge)
        dp = [[-1] * (cnt+1) for _ in range(n)]
        adj = [[] for _ in range(n)]
        for a, b, d in paths:
            adj[a].append((b, d))
            adj[b].append((a, d))
        visited = set()

        dp[start][0] = 0
        import heapq
        hp = []
        hp.append((0, start, 0))

        while hp:
            (pcost, u, c) = heapq.heappop(hp)
            if (u, c) in visited:
                continue
            visited.add((u, c))

            for v, d in adj[u]:
                for i in range(max(d-c, 0), cnt+1-c): # to charge somes.
                    c2 = i + c - d
                    cost = i * charge[u] + d + pcost
                    if (dp[v][c2] == -1 or cost < dp[v][c2]) and (v, c2) not in visited:
                        dp[v][c2] = cost
                        heapq.heappush(hp, (cost, v, c2))

        ans = (1 << 30)
        for v in dp[end]:
            if v == -1: continue
            ans = min(ans, v)
        return ans

cases = [
    ([[1,3,3],[3,2,1],[2,1,3],[0,1,4],[3,0,5]], 6, 1, 0,  [2,10,4,1], 43),
    ([[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]], 8, 0, 2, [4,1,1,3,2], 38),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().electricCarPlan, cases)


if __name__ == '__main__':
    pass
