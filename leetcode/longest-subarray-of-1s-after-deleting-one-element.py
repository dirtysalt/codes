#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        st = [0]
        c = 0
        z = 0
        ans = 0
        for x in nums:
            if x == 1:
                z = 0
                c += 1
                ans = max(st[-1] + c, ans)
                continue

            z += 1
            if z == 1:
                st.append(c)
                c = 0
            else:
                st = [0]

        if ans == len(nums):
            ans -= 1
        return ans
