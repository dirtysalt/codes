#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                if target <= nums[e] <= nums[s] <= nums[m]:
                    s = m + 1
                else:
                    e = m - 1
            else:
                if nums[m] <= nums[e] <= nums[s] <= target:
                    e = m - 1
                else:
                    s = m + 1
        return -1
