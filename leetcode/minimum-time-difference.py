#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tmp = []
        for t in timePoints:
            h = int(t[:2])
            m = int(t[3:])
            v = h * 60 + m
            tmp.append(v)

        tmp.sort()
        ans = tmp[0] + 60 * 24 - tmp[-1]
        for i in range(1, len(tmp)):
            ans = min(ans, tmp[i] - tmp[i - 1])
        return ans
