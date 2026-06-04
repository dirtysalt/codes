#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        dist = [-1] * (n+1)
        import heapq
        hp = []

        adj = [[] for _ in range(n+1)]
        for x, y, d in edges:
            adj[x].append((y, d))
            adj[y].append((x, d))

        acc  = [0] * (n+1)
        acc[n] = 1
        hp.append((0, n))
        while hp:
            (d, x) = heapq.heappop(hp)
            if dist[x] != -1: continue
            dist[x] = d
            for y, d2 in adj[x]:
                if dist[y] == -1:
                    heapq.heappush(hp, (d + d2, y))
                else:
                    # x -> y .. n
                    if dist[x] > dist[y]:
                        acc[x] += acc[y]
#            print(x, acc[x])

#        print(acc, dist)
        MOD = 10 ** 9 + 7
        ans = acc[1] % MOD
        return ans

import aatest_helper

cases = [
    (5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]], 3),
    (7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]], 1),
    (6,[[2,4,5],[3,4,2],[2,1,3],[3,1,3],[4,6,5],[5,1,9],[1,4,3],[2,6,5],[5,6,5],[5,3,8],[1,6,6],[3,2,8],[5,2,8]], 4)
]

aatest_helper.run_test_cases(Solution().countRestrictedPaths, cases)
