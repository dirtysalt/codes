#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def fun(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]

            ans = 0
            if s[i] == '1':
                # try 1 and 10-19.
                ans = fun(i + 1)
                if (i + 1) < len(s):
                    ans += fun(i + 2)
            elif s[i] == '2':
                # try 2 and 20-26
                ans = fun(i + 1)
                if (i + 1) < len(s) and s[i + 1] in '0123456':
                    ans += fun(i + 2)
            else:  # 3-9
                ans = fun(i + 1)

            dp[i] = ans
            return ans

        ans = fun(0)
        return ans
