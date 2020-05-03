#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        dp = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
        for x, y in mines:
            for d in range(4):
                dp[x][y][d] = 0

        def fun(i, j, d, dx, dy):
            if i < 0 or i >= N or j < 0 or j >= N:
                return 0

            if dp[i][j][d] != -1:
                return dp[i][j][d]

            ii, jj = i + dx, j + dy
            ans = 1 + fun(ii, jj, d, dx, dy)
            dp[i][j][d] = ans
            return ans

        ans = 0
        for i in range(N):
            for j in range(N):
                order = N
                for d, (dx, dy) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    t = fun(i, j, d, dx, dy)
                    order = min(order, t)
                ans = max(ans, order)
        return ans
