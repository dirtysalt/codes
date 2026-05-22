#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(high):
            j = i + zero
            if j <= high:
                dp[j] += dp[i]
            j = i + one
            if j <= high:
                dp[j] += dp[i]

        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(low, high + 1):
            ans += dp[i]

        return ans % MOD


if __name__ == '__main__':
    pass
