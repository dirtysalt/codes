#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        S = s  # !!!

        def test(sz):
            t = sum(nums[:sz])
            if t >= S:
                return True
            for i in range(sz, len(nums)):
                t += nums[i] - nums[i - sz]
                if t >= S:
                    return True
            return False

        s, e = 1, len(nums)
        while s <= e:
            sz = (s + e) // 2
            ok = test(sz)
            # print(sz, ok)
            if ok:
                e = sz - 1
            else:
                s = sz + 1

        ans = s
        if ans == len(nums) + 1:
            ans = 0
        return ans
