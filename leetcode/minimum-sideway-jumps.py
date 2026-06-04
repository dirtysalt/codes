#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        import heapq
        n = len(obstacles)
        dp = [[-1] * 4 for _ in range(n)]

        hp = []
        hp.append((0, 0, 2))
        dp[0][2] = 0

        while hp:
            (c, i, w) = heapq.heappop(hp)
            if c != dp[i][w] or i == (n-1):
                continue

            c = dp[i][w]
            if obstacles[i+1] != w:
                if dp[i+1][w] == -1 or dp[i+1][w] > c:
                    dp[i+1][w] = c
                    heapq.heappush(hp, (c, i+1, w))

            for j in range(1, 4):
                if j == w: continue
                if obstacles[i] != j:
                    if dp[i][j] == -1 or dp[i][j] > (c + 1):
                        dp[i][j] = (c  + 1)
                        heapq.heappush(hp, (c+1, i, j))

        ans = 1 << 30
        for i in range(1, 4):
            if dp[-1][i] != -1:
                ans = min(ans, dp[-1][i])
        return ans

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        from collections import deque
        dq = deque()
        n = len(obstacles)
        dp = [[-1] * 4 for _ in range(n)]

        dq.append((0, 2))
        dp[0][2] = 0


        while dq:
            (i, w) = dq.popleft()
            if i == (n-1):
                continue

            c = dp[i][w]
            if obstacles[i+1] != w:
                if dp[i+1][w] == -1 or dp[i+1][w] > c:
                    dp[i+1][w] = c
                    dq.append((i+1, w))

            for j in range(1, 4):
                if j == w: continue
                if obstacles[i] != j:
                    if dp[i][j] == -1 or dp[i][j] > (c + 1):
                        dp[i][j] = (c  + 1)
                        dq.append((i, j))

        ans = 1 << 30
        for i in range(1, 4):
            if dp[-1][i] != -1:
                ans = min(ans, dp[-1][i])
        return ans

cases = [
    ([0,1,2,3,0], 2),
    ([0,1,1,3,3,0], 0),
    ([0,2,1,0,3,0], 2),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minSideJumps, cases)


if __name__ == '__main__':
    pass
