#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        import heapq
        q = []
        n, m = len(grid), len(grid[0])
        dist = [[-1] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        q.append((dist[0][0], 0, 0))
        while q:
            (d, x, y) = heapq.heappop(q)
            for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and dist[x2][y2] == -1:
                    dist[x2][y2] = d + grid[x2][y2]
                    heapq.heappush(q, (dist[x2][y2], x2, y2))

        return health > dist[n - 1][m - 1]


if __name__ == '__main__':
    pass
