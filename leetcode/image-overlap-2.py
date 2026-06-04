#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)

        def check(i, j, A, B):
            res = 0
            for r in range(n - i):
                for c in range(n - j):
                    if A[r][c] == B[r + i][c + j] == 1:
                        res += 1
            return res

        ans = 0
        for i in range(n):
            for j in range(n):
                res = check(i, j, A, B)
                ans = max(res, ans)
                res = check(i, j, B, A)
                ans = max(res, ans)
        return ans
