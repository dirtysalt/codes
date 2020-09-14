#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        ans = 0
        for i in range(len(A) - 2):
            if A[i] < (A[i + 1] + A[i + 2]):
                ans = A[i] + A[i + 1] + A[i + 2]
                break
        return ans
