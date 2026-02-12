#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1

        def issqrt(x):
            s = int(round(x ** 0.5))
            return s * s == x

        for st in range(1 << n):
            first = set()
            # 这里的解决办法是，如果st以相同值结尾的话，那么只保留一份
            for i in range(n):
                if st & (1 << i):
                    if A[i] in first:
                        dp[st][i] = 0
                    else:
                        first.add(A[i])

            for i in range(n):
                if not st & (1 << i): continue
                for j in range(n):
                    if st & (1 << j): continue
                    x = A[i] + A[j]
                    if issqrt(x):
                        dp[st | (1 << j)][j] += dp[st][i]

        ans = 0
        for i in range(n):
            ans += dp[(1 << n) - 1][i]
        return ans


cases = [
    ([2, 2, 2], 1),
    ([1, 17, 8], 2),
    ([1, 1, 8, 1, 8], 1),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().numSquarefulPerms, cases)
