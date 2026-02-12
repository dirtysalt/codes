#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        import functools

        @functools.cache
        def isprime(x):
            if x == 1: return False
            for z in range(2, x):
                if x % z == 0: return False
            return True

        ps = []
        for i in range(len(nums)):
            x = nums[i]
            if isprime(x):
                ps.append(i)

        return ps[-1] - ps[0]


if __name__ == '__main__':
    pass
