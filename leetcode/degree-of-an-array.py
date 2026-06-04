#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        interval = dict()
        counter = Counter()
        n = len(nums)
        for i in range(n):
            x = nums[i]
            counter[x] += 1
            if x not in interval:
                interval[x] = [i, i]
            interval[x][-1] = i

        tops = counter.most_common()
        ans = n
        for x, c in tops:
            if c == tops[0][1]:
                i, j = interval[x]
                res = j - i + 1
                ans = min(ans, res)
            else:
                break

        return ans
