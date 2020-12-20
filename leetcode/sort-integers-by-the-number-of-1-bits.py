#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bits(x):
            ans = 0
            while x:
                if x & 0x1:
                    ans += 1
                x >>= 1
            return ans

        tmp = [(bits(x), x) for x in arr]
        tmp.sort()
        ans = [x[1] for x in tmp]
        return ans
