#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def dist(i):
            return abs(x - points[i][0]) + abs(y - points[i][1])

        ans = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                if ans == -1:
                    ans = i
                elif dist(i) < dist(ans):
                    ans = i

        return ans
