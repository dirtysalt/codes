#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :type fee: int
#         :rtype: int
#         """
#
#         n = len(prices)
#         i = 0
#         ans = 0
#         while i < n:
#             j = i + 1
#             while j < n and prices[j] > prices[j - 1]:
#                 j += 1
#             j -= 1
#             if j != i:
#                 ans += prices[j] - prices[i]
#             i = j + 1
#         return ans

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        ans = 0
        a = prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            if p > a:
                ans += (p - a)
            a = p
        return ans
