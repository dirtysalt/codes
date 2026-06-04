#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        points = [tuple(x) for x in points]

        def test(corner):
            assert len(corner) == 4
            corner.sort()
            rem = set(corner)
            p0, p1, p2, p3 = corner
            if p0[0] != p1[0] or p2[0] != p3[0]: return -1
            if p0[1] != p2[1] or p1[1] != p3[1]: return -1
            x0, x1 = p0[0], p2[0]
            y0, y1 = p0[1], p1[1]
            # print(corner, rem)
            for (x, y) in points:
                if (x, y) in rem: continue
                if x0 <= x <= x1 and y0 <= y <= y1: return -1
            return (x1 - x0) * (y1 - y0)

        import itertools
        ans = -1
        for pts in itertools.combinations(points, 4):
            res = test(list(pts))
            ans = max(ans, res)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1], [1, 3], [3, 1], [3, 3]], 4),
    ([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]], -1),
    ([[1, 1], [1, 3], [3, 1], [3, 3], [1, 2], [3, 2]], 2),
]

aatest_helper.run_test_cases(Solution().maxRectangleArea, cases)

if __name__ == '__main__':
    pass
