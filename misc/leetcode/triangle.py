#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        n = len(triangle)
        dp = [[0] * n for _ in range(2)]
        now = 0

        dp[now][0] = triangle[0][0]
        inf = 1 << 30
        for i in range(1, n):
            k = i + 1
            for j in range(k):
                res = inf
                if j > 0:
                    res = min(res, dp[now][j - 1])
                if (j + 1) < k:
                    res = min(res, dp[now][j])
                dp[1 - now][j] = res + triangle[i][j]
            now = 1 - now

        return min(dp[now])


if __name__ == '__main__':
    sol = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(sol.minimumTotal(triangle))
