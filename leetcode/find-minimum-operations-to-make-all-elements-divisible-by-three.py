#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def cnt(x):
            a = x % 3
            return min(a, 3 - a)

        ans = 0
        for x in nums:
            ans += cnt(x)
        return ans


if __name__ == '__main__':
    pass
