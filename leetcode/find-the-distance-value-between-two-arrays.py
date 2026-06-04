#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        Min, Max = min(arr2), max(arr2)
        ans = 0
        for x in arr1:
            ok = True
            for y in arr2:
                if abs(x - y) <= d:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans
