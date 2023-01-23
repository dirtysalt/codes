#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, n):
            x2, y2 = coordinates[i]
            # y2 - y1 / x2 - x1 = y1 - y0 / x1 - x0
            a = (y2-y1) * (x1-x0)
            b = (y1-y0) * (x2 - x1)
            if a != b:
                return False
        return True


cases = [
    ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
    ( [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().checkStraightLine, cases)
