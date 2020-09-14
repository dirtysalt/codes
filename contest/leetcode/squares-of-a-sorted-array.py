#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        i, j = 0, len(A) - 1
        k = len(A) - 1
        x = A[i] * A[i]
        y = A[j] * A[j]
        while i <= j:   
            if x > y:
                ans[k] = x
                k -= 1
                i += 1
                x = A[i] * A[i]
            else:
                ans[k] = y
                k -= 1
                j -= 1
                y = A[j] * A[j]
        return ans
