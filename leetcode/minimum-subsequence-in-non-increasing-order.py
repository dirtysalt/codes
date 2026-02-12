#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        t = sum(nums)
        ans = []
        acc = 0
        for x in nums:
            acc += x
            ans.append(x)
            if acc > (t - acc):
                break
        return ans
