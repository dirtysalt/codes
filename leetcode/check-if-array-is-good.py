#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        if nums[-1] != (n - 1) or nums[-2] != (n - 1):
            return False
        for i in range(n - 1):
            if nums[i] != (i + 1):
                return False
        return True


if __name__ == '__main__':
    pass
