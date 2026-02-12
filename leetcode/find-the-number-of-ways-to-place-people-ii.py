#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)

        ans = 0
        for i in range(n - 1):
            miny = -(1 << 63)
            r = 0
            for j in range(i + 1, n):
                y = points[j][1]
                if y > points[i][1] or miny >= y: continue
                miny = y
                r += 1
            ans += r

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1], [2, 2], [3, 3]], 0),
    ([[6, 2], [4, 4], [2, 6]], 2),
    ([[3, 1], [1, 3], [1, 1]], 2),
    ([[0, 1], [1, 3], [6, 1]], 2),
]

aatest_helper.run_test_cases(Solution().numberOfPairs, cases)

if __name__ == '__main__':
    pass
