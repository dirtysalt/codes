#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # C(n,m) = C(n-1,m-1) + C(n-1,m)
        N = n + m - 2
        M = m - 1
        dp = [[0] * (M + 1), [0] * (M + 1)]
        now = 0
        dp[now][0] = 1
        for _ in range(N):
            for x in range(M + 1):
                res = 0
                if x > 0:
                    res += dp[now][x - 1]
                res += dp[now][x]
                dp[1 - now][x] = res
            now = 1 - now
        return dp[now][M]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 2))
