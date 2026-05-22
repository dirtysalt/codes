#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        from sortedcontainers import SortedList
        sl = SortedList()

        for a, b in intervals:
            index = sl.bisect(a) - 1
            if index >= 0:
                end = sl[index]
                assert (end <= a)
                sl.remove(end)
            sl.add(b + 1)

        return len(sl)


true, false, null = True, False, None
cases = [
    ([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]], 3),
    ([[1, 3], [5, 6], [8, 10], [11, 13]], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minGroups, cases)

if __name__ == '__main__':
    pass
