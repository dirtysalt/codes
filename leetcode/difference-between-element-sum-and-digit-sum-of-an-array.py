#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            a += x
            while x:
                b += x % 10
                x = x // 10
        return abs(a - b)
    

if __name__ == '__main__':
    pass
