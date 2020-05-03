#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums: return 0

        points = defaultdict(int)
        for x in nums:
            points[x] += x

        xs = list(points.keys())
        xs.sort()
        n = len(xs)

        dp = [0] * n
        dp[0] = points[xs[0]]
        for i in range(1, n):
            res = points[xs[i]]
            if (xs[i] - xs[i - 1]) == 1:
                a = dp[i - 2] if i >= 2 else 0
                b = dp[i - 3] if i >= 3 else 0
                res += max(a, b)
            else:
                a = dp[i - 1] if i >= 1 else 0
                b = dp[i - 2] if i >= 2 else 0
                res += max(a, b)
            dp[i] = res
        ans = max(dp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [10, 8, 4, 2, 1, 3, 4, 8, 2, 9, 10, 4, 8, 5, 9, 1, 5, 1, 6, 8, 1, 1, 6, 7, 8, 9, 1, 7, 6, 8, 4, 5, 4, 1, 5,
            9, 8, 6, 10, 6, 4, 3, 8, 4, 10, 8, 8, 10, 6, 4, 4, 4, 9, 6, 9, 10, 7, 1, 5, 3, 4, 4, 8, 1, 1, 2, 1, 4, 1, 1,
            4, 9, 4, 7, 1, 5, 1, 10, 3, 5, 10, 3, 10, 2, 1, 10, 4, 1, 1, 4, 1, 2, 10, 9, 7, 10, 1, 2, 7, 5]
    print(sol.deleteAndEarn(nums))
