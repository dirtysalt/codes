#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        value = 1 << 30
        ans = -1
        total = sum(nums)
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            a = acc // (i + 1)
            if (i + 1) == len(nums):
                b = 0
            else:
                b = (total - acc) // (len(nums) - i - 1)
            diff = abs(a - b)
            if diff < value:
                ans = i
                value = diff
        return ans


if __name__ == '__main__':
    pass
