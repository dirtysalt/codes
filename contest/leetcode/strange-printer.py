#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = {}

        def fun(i, j):
            if i > j:
                return 0
            if i == j:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]

            ans = 1 + fun(i + 1, j)  # print once char.

            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    # print i..k
                    # then print i+1..k and k+1..j
                    ans = min(ans, fun(i + 1, k) + fun(k + 1, j))

            dp[(i, j)] = ans
            return ans

        ans = fun(0, len(s) - 1)
        return ans
