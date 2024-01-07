#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        a, b = -1, -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 1: a = i
            if nums[i] == n: b = i

        ans = 0
        if a > b:
            ans += a - b
            b = a
            a = a - 1
        ans += a
        ans += n - 1 - b
        return ans


if __name__ == '__main__':
    pass
