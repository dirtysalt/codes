#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for z in range(n - 1):
            for i in range(n - z - 1):
                nums[i] += nums[i + 1]
                nums[i] %= 10
        return nums[0]


if __name__ == '__main__':
    pass
