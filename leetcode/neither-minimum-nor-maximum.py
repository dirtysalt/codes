#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 2:
            return -1
        return nums[1]


if __name__ == '__main__':
    pass
