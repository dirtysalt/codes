#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ms = meetings.copy()
        ms.sort()
        print(ms)
        f, t = ms[0]
        acc = 0
        for x, y in ms[1:]:
            if x > t:
                acc += (t - f + 1)
                f = x
            t = max(t, y)
        acc += (t - f + 1)
        return max(days - acc, 0)


true, false, null = True, False, None
import aatest_helper

cases = [
    (10, [[5, 7], [1, 3], [9, 10]], 2),
    (5, [[2, 4], [1, 3]], 1),
    (6, [[1, 6]], 0),
    (8, [[3, 4], [4, 8], [2, 5], [3, 8]], 1),
    (57, [[3, 49], [23, 44], [21, 56], [26, 55], [23, 52], [2, 9], [1, 48], [3, 31]], 1),
]

aatest_helper.run_test_cases(Solution().countDays, cases)

if __name__ == '__main__':
    pass
