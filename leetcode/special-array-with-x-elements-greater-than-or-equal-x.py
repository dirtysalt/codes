#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def isX(x):
            c = 0
            for z in nums:
                if z >= x:
                    c += 1
            return c == x

        for x in range(1000):
            if isX(x):
                return x
        return -1
