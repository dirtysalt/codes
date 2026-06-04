#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
maxProfitWA是错误的解法，我的初始想法是
1. 把所有的上涨全部列举出来
2. 看临近的上涨是否可以合并

maxProfitNaive是原始的DP，这种DP的时间复杂度是O(n^2), 空间是O(n).
虽然效率比较低下，但是可以保证正确性。在 `find_testcases` 里面可以用来
查找反例以及进行验证。

maxProfit是最终在maxProfitNaive的改进
1. cost是截止到当前i, 如果以prices[i]成交的话，可以获利多少
2. ans是截止到当前最大的profit.
"""


class Solution:
    def maxProfitNaive(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        n = len(prices)
        dp = [0] * n
        for i in range(1, n):
            min_value = prices[i]
            profit = 0
            for j in range(i - 1, -1, -1):
                min_value = min(min_value, prices[j])
                profit = max(profit, dp[j] + (prices[i] - min_value - fee))
            dp[i] = profit
        return max(dp)

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        n = len(prices)
        ans = 0
        cost = -prices[0]
        for i in range(1, n):
            res = prices[i] - fee + cost
            if res > ans:
                ans = res
            cost = max(cost, ans - prices[i])
        return ans

    # Wrong Solution. But sort of heuristic.
    def maxProfitWA(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        n = len(prices)
        temp = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and prices[j] > prices[j - 1]:
                j += 1
            j -= 1
            if j != i:
                temp.append((prices[i], prices[j]))
            i = j + 1

        if not temp:
            return 0

        # print(temp)
        ans = 0
        x, y = temp[0]
        for i in range(1, len(temp)):
            x2, y2 = temp[i]
            if (y - x2) < fee:
                x, y = x, y2
            else:
                ans += max(y - x - fee, 0)
                x, y = x2, y2
        ans += max(y - x - fee, 0)
        return ans


def find_testcases():
    import numpy as np
    rnd = np.random.RandomState(10)
    sol = Solution()
    while True:
        prices = rnd.randint(1, 10, 6)
        fee = 3
        ans0 = sol.maxProfitNaive(prices, fee)
        ans1 = sol.maxProfitNaive(prices, fee)
        # ans1 = sol.maxProfitWA(prices, fee)
        if ans0 != ans1:
            print('FAILED!! ans0 = {}, ans1 = {}'.format(ans0, ans1))
            print(prices, fee)
            break


if __name__ == '__main__':
    sol = Solution()
    # find_testcases()
    print(sol.maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(sol.maxProfit([9, 8, 7, 1, 2], 3))
    print(sol.maxProfit([4, 5, 2, 4, 3, 3, 1, 2, 5, 4], 1))
