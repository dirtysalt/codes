#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in reversed(range(2, len(A))):
            a, b, c = A[i], A[i - 1], A[i - 2]
            if b + c > a:
                return a + b + c
        return 0
