#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        uf = [-1] * (n + 2)

        def find(x):
            while uf[x] != -1:
                x = uf[x]
            res = x
            while uf[x] != -1:
                r = uf[x]
                uf[x] = res
                x = r
            return res

        def merge(a, b):
            a, b = find(a), find(b)
            if a != b:
                uf[a] = b

        for i in range(n):
            ox, oy, r = circles[i]
            if ox - r <= 0 or oy + r >= Y:
                merge(i, n)
            if ox + r >= X or oy - r <= 0:
                merge(i, n + 1)

            for j in range(i):
                x2, y2, r2 = circles[j]
                if (ox - x2) ** 2 + (oy - y2) ** 2 <= (r + r2) ** 2:
                    merge(i, j)

            if find(n) == find(n + 1):
                return False
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(X=3, Y=4, circles=[[2, 1, 1]], res=True),
    aatest_helper.OrderedDict(X=3, Y=3, circles=[[1, 1, 2]], res=false),
    aatest_helper.OrderedDict(X=3, Y=3, circles=[[2, 1, 1], [1, 2, 1]], res=false),
    (5, 8, [[4, 7, 1]], false),
    (6, 6, [[5, 2, 3], [4, 4, 3], [5, 5, 6], [1, 4, 2], [3, 1, 6]], false),
]

aatest_helper.run_test_cases(Solution().canReachCorner, cases)

if __name__ == '__main__':
    pass
