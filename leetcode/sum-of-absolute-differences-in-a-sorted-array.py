#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tt = sum(nums)
        acc = 0
        ans = []
        for i in range(len(nums)):
            x = nums[i]
            acc += x
            a = x * (i + 1) - acc
            b = tt - acc - x * (len(nums) - i - 1)
            ans.append(a + b)
        return ans
