#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        def dot(x, y, z):
            return (z[0] - x[0]) * (y[0] - x[0]) + (z[1] - x[1]) * (y[1] - x[1])

        # p1 (p2, p3), (p3, p4), (p2, p4)
        def test(p1, p2, p3, p4):
            d0 = dot(p1, p2, p3)
            d1 = dot(p4, p2, p3)
            print(d0, d1)

            if d0 == d1 == 0:
                if dist(p1, p2) == dist(p1, p3) == dist(p4, p2) == dist(p4, p3) and dist(p1, p2) > 0:
                    return True
            return False

        if test(p1, p2, p3, p4) or test(p1, p3, p4, p2) or test(p1, p2, p4, p3):
            return True
        return False
