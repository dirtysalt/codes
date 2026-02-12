#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        MOD = 10 ** 9 + 7
        dp[0] = 1

        for i in range(n):
            dp[i] = dp[i] % MOD
            if s[i] == '1':
                dp[i + 1] += dp[i]  # 1 xxx

                if (i + 1) < n:
                    if s[i + 1] == '*':  # 11-19 xxx
                        dp[i + 2] += 9 * dp[i]
                    else:  # 10-19 xxx
                        dp[i + 2] += dp[i]

            elif s[i] == '2':
                dp[i + 1] += dp[i]  # 2 xxx

                if (i + 1) < n:
                    if s[i + 1] in '0123456':  # 20-26 xxx
                        dp[i + 2] += dp[i]
                    elif s[i + 1] == '*':  # 21-26 xxx
                        dp[i + 2] += dp[i] * 6

            elif s[i] == '*':
                dp[i + 1] += dp[i] * 9  # 1-9 xxx

                if (i + 1) < n:
                    if s[i + 1] in '0123456':  # as 20-26 xxx
                        dp[i + 2] += dp[i]
                    if s[i + 1] in '0123456789':  # as 10-19 xxx
                        dp[i + 2] += dp[i]
                    if s[i + 1] == '*':  # as 11-26 but not 20 xxx
                        dp[i + 2] += 15 * dp[i]

            elif s[i] == '0':
                pass

            else:
                dp[i + 1] += dp[i]  # 3-9 xxx

        ans = dp[-1]
        ans = ans % MOD
        return ans
