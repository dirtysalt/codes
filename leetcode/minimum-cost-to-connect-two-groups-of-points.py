#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n, m = len(cost), len(cost[0])
        inf = 1 << 30
        dp = [[inf] * (1 << m) for _ in range(n + 1)]
        dp[0][0] = 0

        C = [[0] * (1 << m) for _ in range(n)]
        for i in range(n):
            for st in range(1 << m):
                c = 0
                for j in range(m):
                    if (st >> j) & 0x1:
                        c += cost[i][j]
                C[i][st] = c
        # print(C)

        for i in range(n):
            for st in range(1 << m):
                val = dp[i][st]
                # 选择至少一个元素
                for j in range(m):
                    st2 = st | (1 << j)
                    dp[i + 1][st2] = min(dp[i + 1][st2], val + cost[i][j])

                # 尝试多个元素去匹配，但是如果已经选择的话就不需要在选择了
                x = R = (1 << m) - 1 - st
                while x:
                    c = C[i][x]
                    st2 = st | x
                    dp[i + 1][st2] = min(dp[i + 1][st2], val + c)
                    x = (x - 1) & R
        ans = dp[n][(1 << m) - 1]
        return ans


class Solution2:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n, m = len(cost), len(cost[0])
        inf = 1 << 30
        dp = [[inf] * (1 << m) for _ in range(n + 1)]
        C = [min(cost[j][i] for j in range(n)) for i in range(m)]
        dp[0][0] = 0

        for i in range(n):
            for st in range(1 << m):
                val = dp[i][st]
                # 选择至少一个元素, 确保i匹配上
                for j in range(m):
                    st2 = st | (1 << j)
                    dp[i + 1][st2] = min(dp[i + 1][st2], val + cost[i][j])

        ans = inf
        for st in range(1 << m):
            c = 0
            for i in range(m):
                if (st >> i) & 0x1: continue
                c += C[i]
            ans = min(ans, dp[n][st] + c)
        return ans


cases = [
    ([[15, 96], [36, 2]], 17),
    ([[1, 3, 5], [4, 1, 1], [1, 5, 3]], 4),
    ([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]], 10),
    ([[44, 91, 93, 34, 50], [100, 92, 72, 86, 24], [72, 62, 91, 74, 19], [37, 64, 9, 16, 13], [99, 55, 23, 21, 16],
      [34, 34, 14, 70, 49], [99, 44, 13, 86, 38], [32, 74, 97, 24, 3], [97, 7, 24, 37, 78], [8, 29, 40, 13, 51],
      [94, 12, 53, 52, 80], [53, 93, 55, 66, 45]], 204),
    ([[11, 18, 21, 37, 45, 77, 45, 19, 82, 97], [88, 56, 71, 64, 6, 3, 39, 40, 73, 30],
      [45, 66, 40, 55, 47, 66, 11, 25, 89, 53], [65, 64, 73, 14, 20, 77, 37, 34, 3, 10],
      [31, 20, 74, 29, 65, 39, 66, 7, 11, 27], [44, 50, 68, 35, 85, 43, 29, 90, 29, 95],
      [75, 35, 79, 28, 33, 32, 47, 63, 94, 48], [47, 73, 43, 3, 97, 52, 83, 90, 66, 8],
      [84, 6, 7, 75, 46, 83, 7, 88, 96, 81], [76, 21, 78, 34, 26, 23, 46, 55, 90, 58],
      [97, 50, 26, 19, 89, 90, 5, 20, 13, 13]], 139),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().connectTwoGroups, cases)
aatest_helper.run_test_cases(Solution2().connectTwoGroups, cases)
