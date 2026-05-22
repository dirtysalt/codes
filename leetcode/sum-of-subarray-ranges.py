#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            a = nums[i]
            b = nums[i]
            for j in range(i + 1, n):
                a = max(a, nums[j])
                b = min(b, nums[j])
                ans += (a - b)

        return ans


if __name__ == '__main__':
    pass
