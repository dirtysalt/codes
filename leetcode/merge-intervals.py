#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for a, b in intervals:
            tmp = []
            added = False
            for c, d in ans:
                if b < c:
                    tmp.append((a, b))
                    added = True

                if b < c or a > d:
                    tmp.append((c, d))
                else:
                    a, b = min(a, c), max(b, d)
            if not added:
                tmp.append((a, b))
            ans = tmp
        return ans
