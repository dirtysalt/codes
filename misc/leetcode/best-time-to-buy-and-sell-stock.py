#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        minv = prices[0]
        ans = 0
        for i in range(1, n):
            minv = min(minv, prices[i])
            diff = prices[i] - minv
            ans = max(ans, diff)
        return ans
