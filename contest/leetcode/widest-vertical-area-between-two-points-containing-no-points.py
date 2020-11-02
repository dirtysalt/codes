#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for i in range(1, len(points)):
            d = points[i][0] - points[i - 1][0]
            ans = max(ans, d)
        return ans
