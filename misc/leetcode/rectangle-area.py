#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        fx = max(A, E)
        tx = min(C, G)
        fy = max(F, B)
        ty = min(D, H)

        area1 = (D - B) * (C - A)
        area2 = (G - E) * (H - F)

        area = area1 + area2
        if (tx - fx) > 0 and (ty - fy) > 0:
            area -= (tx - fx) * (ty - fy)
        return area
