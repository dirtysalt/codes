#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        nm = n * m
        cnt = [0] * nm
        for i, j in indices:
            for k in range(m):
                x = i * m + k
                cnt[x] += 1
            for k in range(n):
                x = k * m + j
                cnt[x] += 1
            # x = i * m + j
            # cnt[x] -= 1

        print(cnt)
        ans = 0
        for x in cnt:
            if x % 2 == 1:
                ans += 1
        return ans
