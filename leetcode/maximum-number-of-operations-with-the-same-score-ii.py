#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @functools.cache
        def f(r, i, j):
            if (j - i) < 1: return 0

            ans = 0
            if nums[i] + nums[j] == r:
                c = f(r, i + 1, j - 1)
                ans = max(ans, c + 1)
            if nums[i] + nums[i + 1] == r:
                c = f(r, i + 2, j)
                ans = max(ans, c + 1)
            if nums[j - 1] + nums[j] == r:
                c = f(r, i, j - 2)
                ans = max(ans, c + 1)
            return ans

        a = f(nums[0] + nums[1], 2, len(nums) - 1)
        b = f(nums[0] + nums[-1], 1, len(nums) - 2)
        c = f(nums[-2] + nums[-1], 0, len(nums) - 3)
        return max(a, b, c) + 1


if __name__ == '__main__':
    pass
