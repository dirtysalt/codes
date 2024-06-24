#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                ans += 1
        # print(nums)
        if nums[-2] != 1 or nums[-1] != 1:
            return -1
        return ans


if __name__ == '__main__':
    pass
