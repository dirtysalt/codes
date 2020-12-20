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

        # 预先计算i可选的j
        adj = [[] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                x = A[i] + A[j]
                s = int(round(x ** 0.5))
                if s * s == x:
                    adj[i].append(j)
                    adj[j].append(i)

        for st in range(1 << n):
            for i in range(n):
                if not st & (1 << i): continue
                for j in adj[i]:
                    if st & (1 << j): continue
                    dp[st | (1 << j)][j] += dp[st][i]
        ans = 0
        for i in range(n):
            ans += dp[(1 << n) - 1][i]

        fac = [1] * 20
        for i in range(2, 20):
            fac[i] = fac[i - 1] * i

        # 比如1出现了3次，那么这3次位置其实都是可以互换的
        from collections import Counter
        cnt = Counter(A)
        for k, c in cnt.items():
            cn = fac[c]
            assert ans % cn == 0
            ans //= cn

        return ans


cases = [
    ([2, 2, 2], 1),
    ([1, 17, 8], 2),
    ([1, 1, 8, 1, 8], 1),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().numSquarefulPerms, cases)
