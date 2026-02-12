#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [0] * 32
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    bits[i] += 1
        n = len(nums)
        ans = 0
        for x in bits:
            ans += x * (n - x)
        return ans
