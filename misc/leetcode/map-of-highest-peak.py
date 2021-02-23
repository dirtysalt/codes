#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        ans = [[0] * m for _ in range(n)]

        hp = []
        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    hp.append((1, i, j))
        import heapq
        heapq.heapify(hp)

        while hp:
            (h, i, j) = heapq.heappop(hp)
            if ans[i][j] != 0: continue
            ans[i][j] = h
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and ans[x][y] == 0:
                    hp.append((h + 1, x, y))

        for i in range(n):
            for j in range(m):
                ans[i][j] -= 1
        return ans


cases = [
    ([[0, 1], [0, 0]], [[1, 0], [2, 1]]),
    ([[0, 0, 1], [1, 0, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 1], [1, 2, 2]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().highestPeak, cases)
