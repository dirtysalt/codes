#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        a = self._countPyramids(grid)
        b = self._countPyramids(list(reversed(grid)))
        return a + b

    def _countPyramids(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        acc = [[0] * (m + 1) for _ in range(n)]
        hs = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                acc[i][j + 1] = acc[i][j] + grid[i][j]

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                h = 1
                if i > 0 and grid[i - 1][j] == 1:
                    h = hs[i - 1][j] - 1

                while True:
                    j2 = j - h
                    j3 = j + h
                    ok = False
                    if 0 <= j2 < m and 0 <= j3 < m and (i + h) < n:
                        dist = (j3 - j2 + 1)
                        ones = acc[i + h][j3 + 1] - acc[i + h][j2]
                        if ones == dist:
                            ok = True
                    if ok:
                        h += 1
                    else:
                        break

                hs[i][j] = h
                ans += (h - 1)

        # print(hs)
        return ans


true, false, null = True, False, None
cases = [
    ([[0, 1, 1, 0], [1, 1, 1, 1]], 2),
    ([[1, 1, 1], [1, 1, 1]], 2),
    ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 0,)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPyramids, cases)

if __name__ == '__main__':
    pass
