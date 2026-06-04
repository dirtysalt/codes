#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        M = max(nums)
        t = 0
        ans = 0

        for x in nums:
            if x == M:
                t += 1
            else:
                ans = max(ans, t)
                t = 0
        ans = max(ans, t)
        return ans


if __name__ == '__main__':
    pass
