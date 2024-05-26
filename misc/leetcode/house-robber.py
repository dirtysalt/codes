#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n + 1)]
        for i in range(n):
            # dp[i][0] is not choosen
            # dp[i][1] is choosen
            dp[i + 1][0] = max(dp[i][0], dp[i][1])
            dp[i + 1][1] = nums[i] + dp[i][0]

        return max(dp[-1])


if __name__ == '__main__':
    pass
