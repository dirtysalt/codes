#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        cnt = [0] * n

        for i in range(n):
            for j in reversed(range(i)):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == 1:
                cnt[i] = 1
            else:
                for j in reversed(range(i)):
                    if nums[i] > nums[j] and dp[i] == (dp[j] + 1):
                        cnt[i] += cnt[j]
        max_len = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == max_len:
                ans += cnt[i]
        return ans
