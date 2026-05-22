#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        from sortedcontainers import SortedList
        s1, s2 = SortedList(), SortedList()
        for (x, y) in points:
            s1.add(x + y)
            s2.add(x - y)

        ans = 1 << 30
        for (x, y) in points:
            s1.remove(x + y)
            s2.remove(x - y)
            a = s1[-1] - s1[0]
            b = s2[-1] - s2[0]
            ans = min(ans, max(a, b))
            s1.add(x + y)
            s2.add(x - y)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[3, 10], [5, 15], [10, 2], [4, 4]], 12),
    ([[1, 1], [1, 1], [1, 1]], 0),
]

aatest_helper.run_test_cases(Solution().minimumDistance, cases)

if __name__ == '__main__':
    pass
