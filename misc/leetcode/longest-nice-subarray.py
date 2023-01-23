#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        x1 = [0] * 32

        def update(x, delta=1):
            for i in range(32):
                if (x & (1 << i)):
                    x1[i] += delta

        def ok():
            for i in range(32):
                if x1[i] > 1: return False
            return True

        j = 0
        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            update(x, 1)
            while not ok():
                update(nums[j], -1)
                j += 1
            size = (i - j + 1)
            ans = max(ans, size)
        return ans


if __name__ == '__main__':
    pass
