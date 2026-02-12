#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [[0] * 32, [0] * 32]
        ans = 0
        for x in nums:
            for i in range(32):
                b = (x >> i) & 0x1
                ans += bits[1 - b][i]
                bits[b][i] += 1
        return ans
