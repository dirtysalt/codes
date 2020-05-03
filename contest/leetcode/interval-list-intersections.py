#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        A.sort()
        B.sort()
        i, j = 0, 0

        ans = []
        while i < len(A) and j < len(B):
            if A[i][0] < B[j][0]:
                if A[i][1] <= B[j][1]:
                    res = (B[j][0], A[i][1])
                    i += 1
                else:
                    res = B[j]
                    j += 1
            else:
                if A[i][1] <= B[j][1]:
                    res = A[i]
                    i += 1
                else:
                    res = (A[i][0], B[j][1])
                    j += 1
            (a, b) = res
            if a <= b:
                ans.append(res)
        return ans
