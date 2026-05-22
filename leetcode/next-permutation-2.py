#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        max_value = nums[-1]
        sp = None
        for i in reversed(range(n)):
            max_value = max(max_value, nums[i])
            if nums[i] < max_value:
                sp = i
                break

        if sp is None:
            nums.sort()
            return

        sp2 = None
        for i in reversed(range(sp + 1, n)):
            if nums[sp] < nums[i]:
                if sp2 is None or nums[i] < nums[sp2]:
                    sp2 = i
        nums[sp], nums[sp2] = nums[sp2], nums[sp]
        nums[sp + 1:] = sorted(nums[sp + 1:])
        return
