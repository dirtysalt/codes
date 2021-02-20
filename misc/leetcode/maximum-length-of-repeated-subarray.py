#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        n = len(A)
        m = len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    ans = max(ans, dp[i + 1][j + 1])
        return ans


if __name__ == '__main__':
    sol = Solution()
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(sol.findLength(A, B))
