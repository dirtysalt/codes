#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        print(boxTypes)
        ans = 0
        for c, t in boxTypes:
            c = min(c, truckSize)
            ans += c * t
            truckSize -= c
            if truckSize == 0:
                break
        return ans
