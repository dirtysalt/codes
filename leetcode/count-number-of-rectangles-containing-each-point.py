#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedList
        sl = SortedList()
        for _, y in rectangles:
            sl.add(y)

        events = []
        events = [(x, y, 1) for x, y in rectangles]
        events.extend([(points[i][0], points[i][1], -i) for i in range(len(points))])
        events.sort()

        ans = [0] * len(points)
        for x, y, t in events:
            if t == 1:
                sl.remove(y)
            else:
                idx = sl.bisect_left(y)
                size = len(sl) - idx
                ans[-t] = size
        return ans

true, false, null = True, False, None
cases = [
    ([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]], [2, 1]),
    ([[1, 1], [2, 2], [3, 3]], [[1, 3], [1, 1]], [1, 3]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countRectangles, cases)

if __name__ == '__main__':
    pass
