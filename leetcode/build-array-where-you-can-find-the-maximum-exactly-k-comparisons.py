#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = {}
        P = 10 ** 9 + 7

        # dp[x][y][z] x个元素,y是最大元素,cost=z
        # dp[x-1][1..y-1][z-1] + dp[x-1][y][z] * (1..y)
        def fun(x, y, z):
            # 这里基准情况需要考虑完整，不然很容易出错
            if x == 0 or y == 0 or z == 0:
                return 0
            if x == 1:
                if z == 1:
                    return 1
                return 0

            key = (x, y, z)
            if key in dp:
                return dp[key]

            ans = 0
            for i in range(1, y):
                ans += fun(x - 1, i, z - 1)
            ans += fun(x - 1, y, z) * y
            dp[key] = ans
            return ans

        ans = 0
        for y in range(1, m + 1):
            ans += fun(n, y, k)
        ans = ans % P
        return ans
