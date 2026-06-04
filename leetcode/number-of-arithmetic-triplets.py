#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                d = nums[j] - nums[i]
                for k in range(j + 1, n):
                    d2 = nums[k] - nums[j]
                    if d == d2 == diff:
                        ans += 1
        return ans


if __name__ == '__main__':
    pass
