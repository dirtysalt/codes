#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numOfWays(self, n: int) -> int:
        def ok(a, b):
            x = [a // 9, (a % 9) // 3, a % 3]
            y = [b // 9, (b % 9) // 3, b % 3]
            for i in range(3):
                if x[i] == y[i]:
                    return False
            return True

        def ok2(a):
            x = [a // 9, (a % 9) // 3, a % 3]
            for i in range(3):
                if (i > 0 and x[i] == x[i - 1]) or ((i + 1) < 3 and x[i] == x[i + 1]):
                    return False
            return True

        opts = []
        for i in range(27):
            if ok2(i):
                opts.append(i)
        from collections import defaultdict
        matches = defaultdict(list)
        for i in opts:
            for j in opts:
                if ok(i, j):
                    matches[i].append(j)

        dp = [[0] * 27, [0] * 27]
        now = 0
        for x in opts:
            dp[now][x] = 1

        P = 10 ** 9 + 7
        for _ in range(1, n):
            for j in opts:
                res = 0
                for k in matches[j]:
                    res += dp[now][k]
                res = res % P
                dp[1 - now][j] = res
            now = 1 - now

        ans = 0
        for i in opts:
            ans += dp[now][i]
            ans %= P
        return ans
