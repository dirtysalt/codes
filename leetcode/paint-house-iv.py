#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        n2 = n // 2
        inf = (1 << 63) - 1
        dp = [[inf] * 9 for _ in range(n2)]
        for i in range(3):
            for j in range(3):
                if i == j: continue
                dp[0][i * 3 + j] = cost[0][i] + cost[-1][j]

        pairs = []
        for a in range(9):
            x1, y1 = a // 3, a % 3
            if x1 == y1: continue
            for b in range(9):
                x2, y2 = b // 3, b % 3
                if x2 == y2: continue
                if x1 == x2 or y1 == y2: continue
                pairs.append((a, b))

        # print(len(pairs))

        for i in range(n2 - 1):
            for a, b in pairs:
                x2, y2 = b // 3, b % 3
                dp[i + 1][b] = min(dp[i + 1][b], dp[i][a] + cost[i + 1][x2] + cost[n - 1 - (i + 1)][y2])

        return min(dp[-1])


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, [[3, 5, 7], [6, 2, 9], [4, 8, 1], [7, 3, 5]], 9),
    (6, [[2, 4, 6], [5, 3, 8], [7, 1, 9], [4, 6, 2], [3, 5, 7], [8, 2, 4]], 18)
]

aatest_helper.run_test_cases(Solution().minCost, cases)

if __name__ == '__main__':
    pass
