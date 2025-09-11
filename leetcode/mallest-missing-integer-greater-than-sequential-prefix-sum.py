#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        acc = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            acc += nums[i]

        while acc in s:
            acc += 1
        return acc


if __name__ == '__main__':
    pass
