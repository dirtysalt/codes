#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n == 1: return 1
        dp = [[-1] * n for _ in range(n)]
        cnt = [[0] * n for _ in range(n)]
        for x, y, d in roads:
            dp[x][y] = d
            dp[y][x] = d
            cnt[x][y] = 1
            cnt[y][x] = 1

        MOD = 10 ** 9 + 7
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] == -1 or dp[k][j] == -1:
                        continue

                    res = dp[i][k] + dp[k][j]
                    if dp[i][j] == -1 or res <= dp[i][j]:
                        if dp[i][j] == -1 or res < dp[i][j]:
                            cnt[i][j] = 0
                        cnt[i][j] += cnt[i][k] * cnt[k][j]
                        cnt[i][j] %= MOD
                        dp[i][j] = res

        return cnt[0][n - 1] % MOD


true, false, null = True, False, None
cases = [
    (7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]],
     4),
    (2, [[1, 0, 10]], 1),
    (1, [], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPaths, cases)

if __name__ == '__main__':
    pass
