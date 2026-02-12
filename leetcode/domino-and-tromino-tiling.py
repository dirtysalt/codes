#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numTilings(self, N: int) -> int:
        dp = {}
        P = 10 ** 9 + 7

        def f(i, j):
            if i == 0 and j == 0:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]

            opts = []
            if i == j:
                opts.append((i - 1, j - 1))
                opts.append((i - 2, j - 2))
                opts.append((i - 2, j - 1))
                opts.append((i - 1, j - 2))

            elif i > j:
                opts.append((i - 2, j - 1))
                opts.append((i - 2, j))

            else:
                opts.append((i - 1, j - 2))
                opts.append((i, j - 2))

            ans = 0
            for (x, y) in opts:
                if x >= 0 and y >= 0:
                    ans += f(x, y)

            ans = ans % P
            dp[(i, j)] = ans
            return ans

        ans = f(N, N)
        return ans
