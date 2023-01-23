#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ss = [(intervals[i][0], i) for i in range(len(intervals))]
        ss.sort()

        xs = [x[0] for x in ss]
        ys = [x[1] for x in ss]
        # 如果这里要求解最小下标的话，可以使用它处理
        # for i in reversed(range(1, len(ys))):
        #     ys[i-1] = min(ys[i-1], ys[i])

        ans = []
        for s, e in intervals:
            import bisect
            idx = bisect.bisect_left(xs, e)
            if 0 <= idx < len(ys):
                ans.append(ys[idx])
            else:
                ans.append(-1)
        return ans


cases = [
    ([[1, 2]], [-1]),
    ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
    ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findRightInterval, cases)
