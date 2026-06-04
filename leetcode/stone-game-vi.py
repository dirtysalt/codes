#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        tmp = [(a + b, a, b) for a, b in zip(aliceValues, bobValues)]
        tmp.sort()

        ans = 0
        order = 0
        for i in reversed(range(len(tmp))):
            if order == 0:
                ans += tmp[i][1]
            else:
                ans -= tmp[i][2]
            order = 1 - order

        if ans > 0:
            ans = 1
        elif ans < 0:
            ans = -1

        return ans
