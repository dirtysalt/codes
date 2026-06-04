#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        a = 0
        for x in nums:
            if x & 0x1 == 0:
                a += 1
        return a >= 2


if __name__ == '__main__':
    pass
