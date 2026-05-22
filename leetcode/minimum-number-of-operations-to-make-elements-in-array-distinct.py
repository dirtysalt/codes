#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 3):
            rest = nums[i:]
            if len(set(rest)) == len(rest):
                return i // 3
        return (len(nums) + 2) // 3


if __name__ == '__main__':
    pass
