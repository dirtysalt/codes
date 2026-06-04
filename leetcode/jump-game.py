#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(n):
            if dp[i]:
                for j in reversed(range(i + 1, min(n, nums[i] + i + 1))):
                    if dp[j] == 1:
                        break
                    dp[j] = 1
        return dp[-1] == 1
