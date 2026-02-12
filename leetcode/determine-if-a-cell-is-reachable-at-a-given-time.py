#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        flex = min(dx, dy)
        d = dx + dy - flex
        if d > t: return False
        if t == 1 and d != 1: return False
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    (2, 4, 7, 7, 6, true),
    (3, 1, 7, 3, 3, false),
    (1, 1, 1, 1, 3, true),
    (1, 2, 1, 2, 1, false)
]

aatest_helper.run_test_cases(Solution().isReachableAtTime, cases)

if __name__ == '__main__':
    pass
