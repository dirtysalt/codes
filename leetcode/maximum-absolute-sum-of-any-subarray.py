#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        Min, Max = 0, 0
        acc = 0
        ans = 0
        for x in nums:
            acc += x
            Min = min(Min, acc)
            Max = max(Max, acc)
            ans = max(ans, abs(acc - Min), abs(acc - Max))
        return ans
