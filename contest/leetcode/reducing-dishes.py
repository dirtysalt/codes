#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat = satisfaction
        sat.sort()

        # print(sat)
        p = -1
        for i in range(len(sat)):
            if sat[i] > 0:
                p = i
                break
        if p == -1:
            return 0

        pbase = sum([(i + 1 - p) * sat[i] for i in range(p, len(sat))])
        pdelta = sum(sat[p:])
        # print(pbase, pdelta)
        ans = pbase

        nbase = 0
        ndelta = 0
        for i in reversed(range(p)):
            pbase += pdelta
            ndelta += sat[i]
            nbase += ndelta
            print(pbase, ndelta, nbase)

            ans = max(ans, pbase + nbase)
        return ans
