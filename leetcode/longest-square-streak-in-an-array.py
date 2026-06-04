#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        skip = set()
        ss = set(nums)
        nums.sort()

        ans = -1
        for x in nums:
            if x in skip: continue
            r = 0
            while x in ss:
                r += 1
                skip.add(x)
                x = x * x
            if r > 1:
                ans = max(ans, r)
        return ans


if __name__ == '__main__':
    pass
