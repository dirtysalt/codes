#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        from math import inf
        n = len(nums)
        dp = [[-inf, -inf] for _ in range(n)]
        dp[0][0] = nums[0]

        for i in range(n - 1):
            if dp[i][0] != -inf:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] - nums[i + 1])
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + nums[i + 1])

            if dp[i][1] != -inf:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][1] + nums[i + 1])

        return max(dp[-1])


if __name__ == '__main__':
    pass
