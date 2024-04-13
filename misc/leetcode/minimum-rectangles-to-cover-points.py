#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        ps = points.copy()
        ps.sort(key=lambda x: x[0])
        j = 0
        ans = 0
        for i in range(len(ps)):
            if ps[i][0] - ps[j][0] > w:
                j = i
                ans += 1
        ans += 1
        return ans


if __name__ == '__main__':
    pass
