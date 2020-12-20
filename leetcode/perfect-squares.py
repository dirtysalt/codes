#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def __init__(self):
        self.dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = self.dp
        while len(dp) <= n:
            x = len(dp)
            ans = 1 << 30
            for p in range(1, x + 1):
                p2 = p ** 2
                if p2 > x:
                    break
                ans = min(ans, dp[x - p2] + 1)
            dp.append(ans)
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(34))
    print(sol.numSquares(211))
    print(sol.numSquares(6701))
    print(sol.numSquares(7691))
    print(sol.numSquares(3102))
