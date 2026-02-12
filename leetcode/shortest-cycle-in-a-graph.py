#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        INF = 1 << 30

        def bfs(src, dst):
            from collections import deque
            dq = deque()
            depth = [-1] * n
            dq.append(src)
            depth[src] = 0
            while dq:
                x = dq.popleft()
                if x == dst:
                    return depth[x] + 1
                for y in adj[x]:
                    if depth[y] != -1: continue
                    # exclude this edge.
                    if (x, y) == (src, dst) or (y, x) == (src, dst): continue
                    depth[y] = depth[x] + 1
                    dq.append(y)
            return INF

        ans = INF
        for (src, dst) in edges:
            r = bfs(src, dst)
            ans = min(ans, r)
        if ans == INF: ans = -1

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 3),
    (4, [[0, 1], [0, 2]], -1),
    (8, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 7], [0, 6], [5, 7], [5, 6]], 4),
]

aatest_helper.run_test_cases(Solution().findShortestCycle, cases)

if __name__ == '__main__':
    pass
