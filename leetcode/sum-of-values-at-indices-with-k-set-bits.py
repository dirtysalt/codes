#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0

        for i, x in enumerate(nums):
            c = 0
            while i:
                c += i & 0x1
                i = i >> 1
            if c == k:
                ans += x
        return ans


if __name__ == '__main__':
    pass
