#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        # dp[i][j] day i and city j points
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(k):
            for j in range(n):
                for z in range(n):
                    if j == z:
                        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + stayScore[i][j])
                    else:
                        dp[i + 1][z] = max(dp[i + 1][z], dp[i][j] + travelScore[j][z])

        return max(dp[-1])


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=2, k=1, stayScore=[[2, 3]], travelScore=[[0, 2], [1, 0]], res=3),
    aatest_helper.OrderedDict(n=3, k=2, stayScore=[[3, 4, 2], [2, 1, 2]], travelScore=[[0, 2, 1], [2, 0, 4], [3, 2, 0]],
                              res=8),
]

aatest_helper.run_test_cases(Solution().maxScore, cases)

if __name__ == '__main__':
    pass
