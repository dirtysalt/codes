#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict
from typing import List

from leetcode import aatest_helper


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xindex = defaultdict(set)
        for (x, y) in points:
            xindex[x].add(y)

        xs = list(xindex.keys())
        xs.sort()
        init_ans = 1 << 30
        ans = init_ans
        for i in range(len(xs)):
            ys0 = xindex[xs[i]]
            for j in range(i + 1, len(xs)):
                spx = xs[j] - xs[i]
                ys1 = xindex[xs[j]]
                ys = list(ys0 & ys1)
                ys.sort()
                for u in range(len(ys)):
                    for v in range(u + 1, len(ys)):
                        spy = ys[v] - ys[u]
                        area = spy * spx
                        ans = min(ans, area)
        if ans == init_ans:
            ans = 0
        return ans


cases = [
    ([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]], 4),
    ([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]], 2)
]
sol = Solution()
aatest_helper.run_test_cases(sol.minAreaRect, cases)
