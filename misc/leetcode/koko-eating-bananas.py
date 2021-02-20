#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def test(k):
            h = 0
            for x in piles:
                h += (x + k - 1) // k
            return h

        s, e = 1, max(piles)
        while s <= e:
            m = (s + e) // 2
            h = test(m)
            if h <= H:
                e = m - 1
            else:
                s = m + 1

        ans = s
        return ans
