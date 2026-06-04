#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def in_circle(x, y):
            x2 = (x - x_center)
            y2 = (y - y_center)
            return x2 ** 2 + y2 ** 2 <= radius ** 2

        def in_rect(x, y):
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True
            return False

        pts = [(x_center, y1), (x_center, y2), (x1, y_center), (x2, y_center)]
        pts += [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
        pts += [(x_center + radius, y_center), (x_center - radius, y_center)]
        pts += [(x_center, y_center - radius), (x_center, y_center + radius)]
        for x, y in pts:
            if in_circle(x, y) and in_rect(x, y):
                return True
        return False
