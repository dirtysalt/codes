#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """

    def maxVacationDays(self, flights, days):
        # Write your code here

        N = len(flights)
        K = len(days[0])

        dp = []
        dp.append([-1] * N)
        dp.append([-1] * N)
        dp[0][0] = 0

        curr = 0
        for k in range(K):
            for c in range(N):
                for c2 in range(N):
                    if (c == c2 or flights[c][c2]) and dp[curr][c] >= 0:
                        dp[1 - curr][c2] = max(dp[1 - curr][c2],
                                               dp[curr][c] + days[c2][k])
            curr = 1 - curr

        return max(dp[curr])
