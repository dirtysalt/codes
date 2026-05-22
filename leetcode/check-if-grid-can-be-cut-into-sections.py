#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def handle_pts(pts):
            pts.sort(key=lambda x: (x[0], -x[1]))
            seg = []
            i = 0
            while i < len(pts):
                start = pts[i][1]
                seg.append(start)
                i += 1
                while i < len(pts) and pts[i][0] < start:
                    start = max(start, pts[i][1])
                    i += 1
            # print(seg)
            return len(seg) >= 3

        xs = [[x[0], x[2]] for x in rectangles]
        ys = [[x[1], x[3]] for x in rectangles]
        return handle_pts(xs) or handle_pts(ys)


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]], true),
    (4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]], true),
    (4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]], false)
]

aatest_helper.run_test_cases(Solution().checkValidCuts, cases)

if __name__ == '__main__':
    pass
