#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ps = set(baseCosts)
        for t in toppingCosts:
            ds = set()
            for i in range(2):
                for p in ps:
                    ds.add(p + t)
                    ds.add(p + 2 * t)
            ps.update(ds)

        ans = baseCosts[0]
        for p in ps:
            x = abs(p - target)
            y = abs(ans - target)
            if x < y or (x == y and p < ans):
                ans = p
        return ans
