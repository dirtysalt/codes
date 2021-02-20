#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
这题的动态规划很有意思
1. back[i+1]=j 表示截止到A[i], 那么A[j..i]所有的值都是在[L,R]之间的
2. dp[i+1] 则表示包含A[i]的话，有多少种组合
这里需要计算back的原因是，如果A[i]<L的话，那么只能使用之前的组合
但是如果A[i]在[L,R]范围的话，那么实际选择是有i-back[i]+1中选择的
"""


class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        n = len(A)
        back = [0] * (n + 1)
        dp = [0] * (n + 1)
        for i in range(n):
            if A[i] > R:
                back[i + 1] = i + 1
                dp[i + 1] = 0
            else:
                back[i + 1] = min(i + 1, back[i])
                if A[i] < L:
                    dp[i + 1] = dp[i]
                else:
                    dp[i + 1] = (i - back[i] + 1)
        # print(dp[1:], back[1:])
        ans = 0
        for i in range(n):
            ans += dp[i + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
    print(sol.numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
