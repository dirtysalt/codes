#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        cnt = [0] * m

        ans = 0
        for i in range(n):
            flip = False
            if A[i][0] == 0:
                flip = True
            res = 0
            for j in range(m):
                v = A[i][j]
                if flip:
                    v = 1 - v
                res = res * 2 + v
                if v == 1:
                    cnt[j] += 1
            # print(res)
            ans += res

        for j in range(1, m):
            # zero is more than one.
            # flip this row.
            if (n - cnt[j]) > cnt[j]:
                add = n - cnt[j] * 2
                delta = (1 << (m - j - 1)) * add
                ans += delta
                # print(j, cnt[j], delta)
        return ans
