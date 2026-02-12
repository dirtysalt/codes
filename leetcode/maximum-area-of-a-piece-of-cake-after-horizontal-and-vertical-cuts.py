#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hs = horizontalCuts
        vs = verticalCuts
        hs.extend([0, h])
        vs.extend([0, w])
        hs.sort()
        vs.sort()

        a = 0
        for i in range(1, len(hs)):
            x = hs[i] - hs[i - 1]
            a = max(a, x)
        b = 0
        for i in range(1, len(vs)):
            x = vs[i] - vs[i - 1]
            b = max(b, x)
        MOD = 10 ** 9 + 7
        ans = (a * b) % MOD
        return ans
