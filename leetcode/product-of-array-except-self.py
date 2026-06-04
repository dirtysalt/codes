#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        tmp = 1
        for i in range(n - 1):
            tmp *= nums[i]
            ans[i + 1] *= tmp  # ans[i+1] = nums[0] * ... nums[i]

        tmp = 1
        for i in reversed(range(1, n)):
            tmp *= nums[i]
            ans[i - 1] *= tmp  # ans[i-1] = nums[i] * ... nums[n-1]

        return ans
