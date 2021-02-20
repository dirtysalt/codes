#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect
import random


class Solution:

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        areas = [(x[2] - x[0] + 1) * (x[3] - x[1] + 1) for x in rects]
        for i in range(1, len(areas)):
            areas[i] += areas[i - 1]
        self.areas = areas

    def pick(self):
        """
        :rtype: List[int]
        """
        p = random.randint(1, self.areas[-1])
        area_idx = bisect.bisect_left(self.areas, p)
        rect = self.rects[area_idx]
        point_idx = p - (self.areas[area_idx - 1] if area_idx > 0 else 0) - 1
        width = rect[2] - rect[0] + 1
        py = point_idx // width + rect[1]
        px = point_idx % width + rect[0]
        return [px, py]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
