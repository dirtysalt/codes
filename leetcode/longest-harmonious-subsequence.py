#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = Counter()
        for v in nums:
            counter[v] += 1

        ans = 0
        for v in nums:
            a = counter[v]
            b = counter[v + 1]
            if a and b:
                ans = max(ans, a + b)
        return ans
