#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        x = nums[0]
        for i in range(len(nums)):
            x = gcd(x, nums[i])
            if x == 1:
                return True
        return False
