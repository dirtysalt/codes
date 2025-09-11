#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        M, A = 0, divisors[0]
        for d in divisors:
            c = 0
            for x in nums:
                if x % d == 0:
                    c += 1
            if c > M or (c == M and d < A):
                M = c
                A = d
        return A


if __name__ == '__main__':
    pass
