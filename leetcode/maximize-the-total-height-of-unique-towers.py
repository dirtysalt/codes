#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        hs = sorted(maximumHeight, reverse=True)
        last = hs[0] + 1
        ans = 0
        for h in hs:
            r = h if h < last else (last - 1)
            if r == 0: return -1
            ans += r
            last = r
        return ans


if __name__ == '__main__':
    pass
