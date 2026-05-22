#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def getValue(q, x0, y0, x1, y1):
            dist = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
            if dist > radius:
                return 0
            return int(floor(q / (dist + 1)))

        tmp = []
        for x0, y0, q0 in towers:
            v = 0
            for x1, y1, q1 in towers:
                v += getValue(q1, x0, y0, x1, y1)
            tmp.append((v, (x0, y0)))

        maxv = max((x[0] for x in tmp))
        ans = [x[1] for x in tmp if x[0] == maxv]
        ans.sort()
        return ans[0]
