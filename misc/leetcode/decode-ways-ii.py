#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        MOD = 10 ** 9 + 7

        def fun(i):
            if i == n:
                return 1

            key = i
            if key in dp:
                return dp[key]

            ans = 0
            if s[i] == '1':
                ans += fun(i + 1)  # 1 xxx

                if (i + 1) < n:
                    if s[i + 1] == '*':  # 11-19
                        ans += 9 * fun(i + 2)  # 11-19 xxx
                    else:
                        ans += fun(i + 2)  # 10-19 xxx

            elif s[i] == '2':
                ans += fun(i + 1)  # 2 xxx

                if (i + 1) < n:
                    if s[i + 1] in '0123456':  # 20-26 xxx
                        ans += fun(i + 2)
                    elif s[i + 1] == '*':  # 21-26 xxx
                        ans += fun(i + 2) * 6

            elif s[i] == '*':
                ans += fun(i + 1) * 9  # 1-9 xxx

                if (i + 1) < n:
                    if s[i + 1] in '0123456':
                        ans += fun(i + 2)  # as 20-26 xxx
                    if s[i + 1] in '0123456789':
                        ans += fun(i + 2)  # as 10-19 xxx
                    if s[i + 1] == '*':  # as 11-26 but not 20 xxx
                        ans += 15 * fun(i + 2)

            elif s[i] == '0':
                return 0

            else:
                ans += fun(i + 1)  # 3-9 xxx

            dp[key] = ans % MOD
            return ans

        ans = fun(0)
        ans = ans % MOD
        return ans
