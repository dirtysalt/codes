#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        inf = 1 << 31
        dp = [inf] * (1 + amount)
        dp[0] = 0
        for x in range(amount):
            for c in coins:
                if x + c > amount:
                    continue
                dp[x + c] = min(dp[x + c], dp[x] + 1)
        if dp[amount] == inf:
            return -1
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    print((s.coinChange([1, 2, 5], 11)))
    print((s.coinChange([2], 3)))
