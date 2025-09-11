#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        acc = 0
        ans = 0
        for x in gain:
            acc = acc + x
            ans = max(ans, acc)
        return ans
