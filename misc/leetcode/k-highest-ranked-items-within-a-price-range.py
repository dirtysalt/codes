#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        n, m = len(grid), len(grid[0])
        (r, c) = start
        (low, high) = pricing
        visited = {}
        pq = []
        pq.append((0, r, c))
        res = []
        while pq:
            (d, r, c) = heapq.heappop(pq)
            if (r, c) in visited:
                continue
            if grid[r][c] > 1 and grid[r][c] >= low and grid[r][c] <= high:
                res.append((d, grid[r][c], r, c))

            visited[(r, c)] = d
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = r + dx, c + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] and (x, y) not in visited:
                    heapq.heappush(pq, (d + 1, x, y))

        res.sort()
        ans = [[x[2], x[3]] for x in res[:k]]
        return ans


true, false, null = True, False, None
cases = [
    ([[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], [2, 5], [0, 0], 3, [[0, 1], [1, 1], [2, 1]]),
    ([[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]], [2, 3], [2, 3], 2, [[2, 1], [1, 2]]),
    ([[1, 1, 1], [0, 0, 1], [2, 3, 4]], [2, 3], [0, 0], 3, [[2, 1], [2, 0]]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().highestRankedKItems, cases)

if __name__ == '__main__':
    pass
