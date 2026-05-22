#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        i, j = 0, n - 1
        ans = 0
        while i < j:
            ans += piles[j - 1]
            j -= 2
            i += 1
        return ans
