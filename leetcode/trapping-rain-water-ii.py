#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])
        visited = set()
        hp = []
        for i in range(n):
            hp.append((heightMap[i][0], i, 0))
            hp.append((heightMap[i][m - 1], i, m - 1))
            visited.add((i, 0))
            visited.add((i, m - 1))
        for i in range(m):
            hp.append((heightMap[0][i], 0, i))
            hp.append((heightMap[-1][i], n - 1, i))
            visited.add((0, i))
            visited.add((n - 1, i))

        import heapq
        heapq.heapify(hp)

        ans = 0
        while hp:
            (h, x, y) = heapq.heappop(hp)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and (x2, y2) not in visited:
                    visited.add((x2, y2))
                    h2 = heightMap[x2][y2]
                    if h > h2:
                        ans += (h - h2)
                    heapq.heappush(hp, (max(h2, h), x2, y2))
        return ans


cases = [
    ([
         [1, 4, 3, 1, 3, 2],
         [3, 2, 1, 3, 2, 4],
         [2, 3, 3, 2, 3, 1]
     ], 4),
    ([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]], 14),
    ([[5, 5, 5, 1], [5, 1, 1, 5], [5, 1, 5, 5], [5, 2, 5, 8]], 3),
    ([[9, 9, 9, 9, 9], [9, 2, 1, 2, 9], [9, 2, 8, 2, 9], [9, 2, 3, 2, 9], [9, 9, 9, 9, 9]], 57),
    ([[5, 8, 7, 7], [5, 2, 1, 5], [7, 1, 7, 1], [8, 9, 6, 9], [9, 8, 9, 9]], 12)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().trapRainWater, cases)
