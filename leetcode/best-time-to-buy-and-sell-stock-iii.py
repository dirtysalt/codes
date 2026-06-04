#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices: return 0

        n = len(prices)
        st = [0] * n

        # st[i]: 从i开始往后交易最多的profit
        max_sell = prices[-1]
        max_profit = 0
        for i in reversed(range(n)):
            max_sell = max(max_sell, prices[i])
            max_profit = max(max_profit, max_sell - prices[i])
            st[i] = max_profit

        ans = 0
        min_buy = prices[0]
        max_profit = 0
        for i in range(n):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy)
            ans = max(ans, max_profit + st[i])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2, 1, 2, 0, 1]))
    print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
