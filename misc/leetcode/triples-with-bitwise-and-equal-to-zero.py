#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        from collections import Counter
        cnt = Counter()
        for i in range(n):
            for j in range(n):
                x = A[i] & A[j]
                cnt[x] += 1

        ans = 0
        for i in range(n):
            x = A[i]
            for y, c in cnt.items():
                if x & y == 0:
                    ans += c
        return ans
