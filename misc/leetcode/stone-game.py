#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        dp = {}

        def fun(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            ans = piles[i] - fun(i + 1, j)
            ans = max(ans, piles[j] - fun(i, j - 1))
            dp[(i, j)] = ans
            return ans

        ans = fun(0, len(piles) - 1)
        return ans > 0
