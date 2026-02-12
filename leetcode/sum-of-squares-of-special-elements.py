#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if n % (i + 1) == 0:
                ans += nums[i] ** 2
        return ans


if __name__ == '__main__':
    pass
