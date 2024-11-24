#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        ans = 0

        import functools
        @functools.cache
        def nextdist(i, j):
            c = 0
            while i != j:
                c += nextCost[i]
                i = (i + 1) % 26
            return c

        @functools.cache
        def prevdist(i, j):
            c = 0
            while i != j:
                c += previousCost[i]
                i = (i - 1 + 26) % 26
            return c

        ans = 0
        for i in range(len(s)):
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            ans += min(nextdist(a, b), prevdist(a, b))
        return ans


if __name__ == '__main__':
    pass
