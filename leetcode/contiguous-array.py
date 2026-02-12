#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        past = {}
        past[0] = -1

        t = 0
        ans = 0
        for i, x in enumerate(nums):
            if x == 1:
                t += 1
            else:
                t -= 1
            if t in past:
                ans = max(ans, i - past[t])
            else:
                past[t] = i
        return ans
