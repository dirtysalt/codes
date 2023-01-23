#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        acc = nums[:]
        dp = []
        for i in range(n):
            dp.append([None] * n)
        for i in range(1, n):
            acc[i] += acc[i - 1]
        # print(acc)

        for i in range(n):
            dp[i][i] = nums[i]

        inf = 1 << 31
        for k in range(2, n + 1):
            for i in range(0, n - k + 1):
                j = i + k - 1
                # [i .. j] depends on [i+1..j] and [i..j-1]
                value = max((acc[j] - acc[i]) - dp[i + 1][j] + nums[i],
                            (acc[j - 1] - (acc[i - 1] if i > 0 else 0) - dp[i][j - 1] + nums[j]))
                dp[i][j] = value

        # print(dp)
        a = dp[0][n - 1]
        b = acc[n - 1] - a
        # print(a, b)
        return a >= b


if __name__ == '__main__':
    s = Solution()
    print(s.PredictTheWinner([1, 5, 2]))
    print(s.PredictTheWinner([1, 5, 233, 7]))
