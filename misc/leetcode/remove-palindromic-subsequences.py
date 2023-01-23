#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0

        if s == s[::-1]:
            return 1

        return 2

    def removePalindromeSub2(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        par = [[0] * n for _ in range(n)]

        for sz in range(1, n + 1):
            for i in range(0, n - sz + 1):
                j = i + sz - 1
                if s[i] == s[j]:
                    if (i + 1) > (j - 1) or par[i + 1][j - 1]:
                        par[i][j] = 1

        dp = [0] * n
        inf = (1 << 30)
        for i in range(n):
            ans = inf
            for j in range(0, i + 1):
                if par[j][i]:
                    res = dp[j - 1] if (j - 1) >= 0 else 0
                    ans = min(ans, res + 1)
            dp[i] = ans

        ans = dp[n - 1]
        return ans
