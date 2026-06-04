#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        N = len(passingFees)
        adj = [[] for _ in range(N)]
        for x, y, t in edges:
            adj[x].append((y, t))
            adj[y].append((x, t))

        import heapq
        hp = []
        hp.append((passingFees[0], 0, 0))
        ans = -1

        best = {}
        inf = 1 << 30

        def update(x, c, t):
            if x not in best:
                best[x] = [inf] * (maxTime + 1)
            arr = best[x]
            if arr[t] > c:
                arr[t] = c
                # also update forward.
                for t0 in range(t + 1, len(arr)):
                    if arr[t0] > c:
                        arr[t0] = c
                    else:
                        break
                return True
            return False

        while hp:
            c, x, t = heapq.heappop(hp)
            if x == N - 1:
                ans = c
                break

            for y, dt in adj[x]:
                t2 = t + dt
                c2 = passingFees[y] + c
                if t2 > maxTime: continue
                # update nodes y
                if update(y, c2, t2):
                    heapq.heappush(hp, (c2, y, t2))

        return ans


true, false, null = True, False, None
cases = [
    (30, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3], 11),
    (29, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3], 48),
    (25, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3], -1),

]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCost, cases)

if __name__ == '__main__':
    pass
