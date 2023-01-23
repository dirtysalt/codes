#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        j = 0
        ans = 0

        def cut(i, j):
            tt = 0
            mx = cost[i]
            for k in range(i, j):
                tt += cost[k]
                mx = max(mx, cost[k])
            return tt - mx

        for i in range(n):
            if s[i] == s[j]: continue
            ans += cut(j, i)
            j = i

        ans += cut(j, n)
        return ans
