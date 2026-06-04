#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here

        def ok(nums, k, avg):
            n = len(nums)
            pre = [0] * n
            acc = 0
            for i in range(n):
                acc += nums[i]
                pre[i] = acc - (i + 1) * avg
            min_pre = 0
            for i in range(k - 1, n):
                # 1..k
                if (pre[i] - min_pre) >= 0:
                    return True
                min_pre = min(min_pre, pre[i - k + 1])
            return False

        min_avg = min(nums)
        max_avg = max(nums)
        while (max_avg - min_avg) > 1e-4:
            avg = (min_avg + max_avg) * 0.5
            if ok(nums, k, avg):
                min_avg = avg
            else:
                max_avg = avg
        return round((max_avg + min_avg) * 0.5, 3)
