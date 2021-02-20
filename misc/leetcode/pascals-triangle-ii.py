#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        dp = [[1] * (rowIndex + 1) for _ in range(2)]
        now = 0

        for k in range(rowIndex):
            n = (k + 2)
            for i in range(1, n - 1):
                dp[1 - now][i] = dp[now][i - 1] + dp[now][i]
            now = 1 - now

        return dp[now]
