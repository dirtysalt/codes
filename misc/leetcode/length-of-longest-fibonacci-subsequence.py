#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        indices = {}
        for i in range(n):
            indices[A[i]] = i
        dp = [[0] * n for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(i):
                # A[k] + A[j] = A[i]
                k = indices.get(A[i] - A[j])
                if k is not None and k < j:
                    dp[i][j] = dp[j][k] + 1 if dp[j][k] != 0 else 3
                    ans = max(ans, dp[i][j])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    print(sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
    print(sol.lenLongestFibSubseq([1, 3, 4, 7, 11, 18]))
