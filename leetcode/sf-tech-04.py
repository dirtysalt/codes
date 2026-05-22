#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isPointInPolygon(self, x: float, y: float, coords: List[float]) -> bool:
        n = len(coords) // 2
        clock = []
        for i in range(1, n):
            x0, y0 = coords[2 * i - 2:i * 2]
            x1, y1 = coords[2 * i:2 * i + 2]
            dx, dy = (x1 - x0, y1 - y0)
            a, b = (x - x0, y - y0)
            v = b * dx - a * dy
            if v == 0: continue
            clock.append(v)

        if all((x < 0 for x in clock)) or all((x > 0 for x in clock)):
            return True
        return False


true, false, null = True, False, None
cases = [
    (1, 3, [0, 0, 0, 4, 4, 4, 2, 2, 4, 0, 0, 0], true)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isPointInPolygon, cases)

if __name__ == '__main__':
    pass
