#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if i - k >= 0 and nums[i] <= nums[i - k]:
                continue
            if (i + k) < len(nums) and nums[i] <= nums[i + k]:
                continue
            ans += nums[i]
        return ans


if __name__ == '__main__':
    pass
