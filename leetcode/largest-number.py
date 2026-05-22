#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all([x == 0 for x in nums]):
            return '0'

        nums = list(map(str, nums))

        def cmp(x, y):
            assert len(x) == len(y)
            res = -1 if x < y else 0
            return res
            
            #
            # if x == y:
            #     return 0
            #
            # for i in range(len(x)):
            #     if x[i] < y[i]:
            #         return -1
            #     elif x[i] > y[i]:
            #         return 1
            # return 0

        # def sort_fn(x, y):
        #     sign = 1
        #     if len(x) > len(y):
        #         x, y = y, x
        #         sign = -1
        #
        #     res = cmp(x, y[:len(x)])
        #     if res != 0:
        #         return res * sign
        #
        #     # 假设y要更长的话, x = a, y = a | b
        #     # 两种排列 a a b 和 a b a
        #     # 所以其实是比较y之后的字符串
        #     szb = len(y) - len(x)
        #     res = cmp(y, y[len(x): len(x) + szb] + x)
        #     return res * sign

        def sort_fn(x, y):
            return cmp(x + y, y + x)

        nums.sort(key=functools.cmp_to_key(sort_fn), reverse=True)
        # print(nums)
        ans = ''.join(nums)
        return ans


cases = [
    ([10, 2], "210"),
    ([3, 30, 34, 5, 9], "9534330"),
    ([121, 12], "12121"),
    ([0, 0], "0")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestNumber, cases)
