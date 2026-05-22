#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        en = [energyDrinkA, energyDrinkB]

        import functools
        @functools.cache
        def dfs(i, ab):
            if i >= n: return 0
            r = en[ab][i]
            a = dfs(i + 1, ab)
            b = dfs(i + 2, 1 - ab)
            return max(a, b) + r

        ans = max(dfs(0, 0), dfs(0, 1))
        return ans


if __name__ == '__main__':
    pass
