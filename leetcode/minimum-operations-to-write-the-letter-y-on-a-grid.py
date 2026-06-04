#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = (n + 1) // 2
        pts = set()

        for i in range(mid):
            pts.add((i, i))
            pts.add((i, n - 1 - i))
        for i in range(mid, n):
            pts.add((i, mid - 1))

        from collections import Counter
        cnt1, cnt2 = Counter(), Counter()
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                if (i, j) in pts:
                    cnt1[x] += 1
                else:
                    cnt2[x] += 1

        # print(cnt1, cnt2)
        ans = 1 << 30
        for a in range(3):
            for b in range(3):
                if a == b: continue
                r0 = len(pts) - cnt1[a]
                r1 = (n * n) - len(pts) - cnt2[b]
                ans = min(ans, r0 + r1)
        return ans


if __name__ == '__main__':
    pass
