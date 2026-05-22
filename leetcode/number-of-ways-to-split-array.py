#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        t = sum(nums)
        p = 0
        ans = 0
        for i in range(0, len(nums) - 1):
            p += nums[i]
            p2 = t - p
            if p >= p2:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
