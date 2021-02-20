#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        par = [[0] * n for _ in range(n)]
        for sz in range(1, n + 1):
            for i in range(0, n - sz + 1):
                j = i + sz - 1
                if i == j:
                    par[i][j] = 1
                    continue

                res = 0
                if s[i] == s[j]:
                    v = par[i + 1][j - 1] if (i + 1) <= (j - 1) else 0
                    res = max(res, v + 2)

                if (i + 1) <= j:
                    res = max(res, par[i + 1][j])

                if i <= (j - 1):
                    res = max(res, par[i][j - 1])

                par[i][j] = res

        ans = par[0][n - 1]
        return ans
