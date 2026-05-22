#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        ss = set()

        i, j = 0, len(nums) - 1
        while i < j:
            x = (nums[i] + nums[j]) / 2
            ss.add(x)
            i, j = i + 1, j - 1

        return len(ss)


if __name__ == '__main__':
    pass
