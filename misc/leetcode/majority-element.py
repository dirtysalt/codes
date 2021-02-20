#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        p = None  # any value.
        c = 0
        for x in nums:
            if c == 0:
                p = x
                c = 1
            elif x == p:
                c += 1
            else:
                c -= 1
        return p
