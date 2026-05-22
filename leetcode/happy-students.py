#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        for i in range(1, n):
            # i is first not selected
            # means i people selected
            if i < nums[i] and i > nums[i - 1]:
                ans += 1

        # select all
        if n > nums[-1]:
            ans += 1
        # select none
        if nums[0] > 0:
            ans += 1

        return ans


if __name__ == '__main__':
    pass
