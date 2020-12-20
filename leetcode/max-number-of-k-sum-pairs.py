#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            c = nums[i] + nums[j]
            if c == k:
                i += 1
                j -= 1
                ans += 1
            elif c > k:
                j -= 1
            else:
                i += 1
        return ans
