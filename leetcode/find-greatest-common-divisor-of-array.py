#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        a, b = nums[0], nums[-1]
        return gcd(a, b)


if __name__ == '__main__':
    pass
