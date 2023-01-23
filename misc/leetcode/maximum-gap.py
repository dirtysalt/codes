#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # 如果是radix sort的话就没有太大意思
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i - 1])
        return ans
