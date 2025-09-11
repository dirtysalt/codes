#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        n, m = len(grid), len(grid[0])

        acc = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            tt = 0
            for j in range(m):
                tt += grid[i][j]
                acc[i + 1][j + 1] = tt
            for j in range(m):
                acc[i + 1][j + 1] += acc[i][j + 1]

        # print(acc)

        def values(r, c, r2, c2):
            a = acc[r2 + 1][c2 + 1] - acc[r2 + 1][c]
            b = acc[r][c2 + 1] - acc[r][c]
            return a - b

        def valid(r, c):
            r2, c2 = r + stampHeight - 1, c + stampWidth - 1
            if 0 <= r2 < n and 0 <= c2 < m:
                return values(r, c, r2, c2) == 0
            return False

        from sortedcontainers import SortedList
        sl = SortedList()
        for r in range(n):
            if r >= stampHeight:
                r2 = r - stampHeight
                for c in range(m):
                    if valid(r2, c):
                        sl.remove(c)
            for c in range(m):
                if valid(r, c):
                    sl.add(c)

            # print(sl)
            # check it can be covered.
            for c in range(m):
                if grid[r][c] == 1: continue
                c2 = max(0, c - stampWidth + 1)
                pos = sl.bisect_left(c2)
                if pos < len(sl) and sl[pos] <= c:
                    pass
                else:
                    return False

        return True


true, false, null = True, False, None
cases = [
    ([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 4, 3, true),
    ( [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],2,2,false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().possibleToStamp, cases)

if __name__ == '__main__':
    pass
