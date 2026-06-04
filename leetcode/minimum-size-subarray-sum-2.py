#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        j = 0
        t = 0
        n = len(nums)
        ans = n + 1
        for i in range(n):
            t += nums[i]

            if t >= s:
                while j <= i and t >= s:
                    t -= nums[j]
                    j += 1
                ans = min(ans, i - j + 2)
        if ans == (n + 1):
            ans = 0
        return ans
