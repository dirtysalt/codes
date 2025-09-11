#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: (abs(x), -x))
        return nums[0]


if __name__ == '__main__':
    pass
