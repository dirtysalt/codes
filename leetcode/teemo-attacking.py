#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        n = len(timeSeries)
        ans = 0
        for i in range(n - 1):
            ans += min(timeSeries[i + 1] - timeSeries[i], duration)
        if n:
            ans += duration
        return ans
