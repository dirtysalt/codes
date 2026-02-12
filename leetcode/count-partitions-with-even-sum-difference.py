#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        ans = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            total -= nums[i]
            if abs(left - total) % 2 == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
