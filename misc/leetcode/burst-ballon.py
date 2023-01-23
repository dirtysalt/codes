#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        # write your code here

        nums = [1] + nums + [1]
        cache = {}

        def compute(s, e):
            if (e - s) <= 1:
                return 0
            key = '{}.{}'.format(s, e)
            if key in cache:
                return cache[key]
            res = 0
            tmp = nums[s] * nums[e]
            for x in range(s + 1, e):
                tmp2 = tmp * nums[x]
                tmp2 += compute(s, x)
                tmp2 += compute(x, e)
                if tmp2 > res:
                    res = tmp2
            cache[key] = res
            return res

        return compute(0, len(nums) - 1)
