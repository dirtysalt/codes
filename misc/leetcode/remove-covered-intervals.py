#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        ans = 0
        for i in range(len(intervals)):
            a, b = intervals[i]
            for j in range(len(intervals)):
                if i == j: continue
                c, d = intervals[j]
                if c <= a and b <= d:
                    ans += 1
                    break
        return len(intervals) - ans
