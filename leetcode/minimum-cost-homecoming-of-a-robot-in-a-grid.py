#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r, c = startPos
        hr, hc = homePos
        dc = 1 if c < hc else -1
        dr = 1 if r < hr else -1
        ans = 0
        while c != hc:
            ans += colCosts[c + dc]
            c += dc
        while r != hr:
            ans += rowCosts[r + dr]
            r += dr
        return ans


if __name__ == '__main__':
    pass
