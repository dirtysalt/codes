#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]

        return -1


if __name__ == '__main__':
    pass
