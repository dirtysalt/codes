#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        ans = 0
        while i < len(nums):
            x = nums[i]
            j = i
            while j < len(nums) and (nums[j] - x) <= k:
                j += 1
            i = j
            ans += 1
        return ans


if __name__ == '__main__':
    pass
