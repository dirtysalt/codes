#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        flip = 0
        for i in range(len(nums)):
            if flip == nums[i]:
                flip = 1 - flip
                ans += 1
        return ans


if __name__ == '__main__':
    pass
