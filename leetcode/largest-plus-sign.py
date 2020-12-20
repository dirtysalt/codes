#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        MS = set()
        for x, y in mines:
            MS.add((x, y))

        import functools
        @functools.lru_cache(None)
        def arms(i, j, dx, dy):
            if not (0 <= i < N and 0 <= j < N):
                return 0
            if (i, j) in MS:
                return 0
            return 1 + arms(i + dx, j + dy, dx, dy)

        ans = 0
        for i in range(N):
            for j in range(N):
                if (i, j) in MS:
                    continue
                a = arms(i, j, -1, 0)
                b = arms(i, j, 1, 0)
                c = arms(i, j, 0, -1)
                d = arms(i, j, 0, 1)
                res = min(a, b, c, d)
                ans = max(ans, res)
        return ans
