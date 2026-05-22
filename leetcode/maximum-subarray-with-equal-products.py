#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            g = gcd(a, b)
            return a * b // g

        sz = 1
        for i in range(len(nums)):
            p = x = g = nums[i]
            for j in range(i + 1, len(nums)):
                p = p * nums[j]
                g = gcd(g, nums[j])
                x = lcm(x, nums[j])
                if p != (g * x):
                    break
                sz = max(sz, j - i + 1)
        return sz


if __name__ == '__main__':
    pass
