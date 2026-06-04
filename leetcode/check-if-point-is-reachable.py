#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        while targetX % 2 == 0:
            targetX = targetX // 2
        while targetY % 2 == 0:
            targetY = targetY // 2

        def GCD(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        g = GCD(targetX, targetY)
        return g == 1


true, false, null = True, False, None
import aatest_helper

cases = [
    (6, 9, false),
    (4, 7, true),
    (536870912, 536870912, true),
]

aatest_helper.run_test_cases(Solution().isReachable, cases)

if __name__ == '__main__':
    pass
