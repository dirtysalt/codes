#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        INF = 1 << 30

        class C:
            def __init__(self):
                self.st = []

            def add(self, p, v):
                while self.st:
                    if self.st[-1][1] >= v:
                        self.st.pop()
                    else:
                        break
                self.st.append((p, v))

            def find(self, p):
                st = self.st
                s, e = 0, len(st) - 1
                while s <= e:
                    m = (s + e) // 2
                    if st[m][0] <= p:
                        e = m - 1
                    else:
                        s = m + 1
                if s >= len(st): return INF
                return st[s][1]

        N, M = len(grid), len(grid[0])
        columns = [C() for _ in range(M)]
        dist = [0] * M
        for i in reversed(range(N)):
            cc = C()
            for j in reversed(range(M)):
                if (i, j) == (N - 1, M - 1):
                    dist[j] = 1
                    cc.add(M - 1, 1)
                    continue

                v = grid[i][j]
                if v == 0:
                    dist[j] = INF
                    continue

                d = cc.find(j + v)
                d2 = columns[j].find(i + v)
                d = min(d, d2)
                dist[j] = d + 1
                cc.add(j, dist[j])

            for j in range(M):
                columns[j].add(i, dist[j])

        ans = dist[0]
        if ans >= INF:
            ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]], 4),
    ([[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]], 3),
    ([[2, 1, 0], [1, 0, 0]], -1),
]

aatest_helper.run_test_cases(Solution().minimumVisitedCells, cases)

if __name__ == '__main__':
    pass
