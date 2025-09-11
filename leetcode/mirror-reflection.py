#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        x, y = 0, 0
        dx, dy = p, q
        eps = 1e-6

        def near(x, y, a, b):
            return abs(a - x) < eps and abs(b - y) < eps

        def eq(x, y):
            return abs(x - y) < eps

        ans = -1
        while True:
            if near(x, y, p, 0):
                ans = 0
                break
            if near(x, y, p, p):
                ans = 1
                break
            if near(x, y, 0, p):
                ans = 2
                break

            if dx > 0:
                tx = (p - x) / dx
            else:
                tx = -x / dx
            if dy > 0:
                ty = (p - y) / dy
            else:
                ty = -y / dy
            t = min(tx, ty)
            x += dx * t
            y += dy * t

            # print('>>>', x, y, dx, dy)
            if eq(x, 0) or eq(x, p):
                dx = -dx
            if eq(y, 0) or eq(y, p):
                dy = -dy

        return ans


cases = [
    (3, 1, 1),
    (14, 11, 2),
    (69, 50, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().mirrorReflection, cases)
