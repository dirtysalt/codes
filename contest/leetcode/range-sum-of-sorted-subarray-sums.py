#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        tmp = []
        n = len(nums)
        for i in range(n):
            t = 0
            for j in range(i, n):
                t += nums[j]
                tmp.append(t)
        tmp.sort()

        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(left - 1, right):
            ans += tmp[i]
            ans = ans % MOD
        return ans
