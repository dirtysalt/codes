#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            tmp = []
            n = len(nums)
            f = 0
            for i in range(0, n, 2):
                if f == 0:
                    x = min(nums[i], nums[i + 1])
                else:
                    x = max(nums[i], nums[i + 1])
                tmp.append(x)
                f = 1 - f
            nums = tmp
        return nums[0]


if __name__ == '__main__':
    pass
