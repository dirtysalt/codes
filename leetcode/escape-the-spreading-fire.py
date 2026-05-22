#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        G = [[0] * m for _ in range(n)]

        from collections import deque
        dq = deque()
        for i in range(n):
            for j in range(m):
                G[i][j] = grid[i][j]
                if G[i][j] == 2:
                    G[i][j] = -1

                if G[i][j] == 1:
                    dq.append((i, j, 1))
                    G[i][j] = 0

        while dq:
            (i, j, d) = dq.popleft()
            if G[i][j] == 0:
                G[i][j] = d
            else:
                continue
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and G[x][y] == 0:
                    dq.append((x, y, d + 1))

        INF = 10 ** 9
        for i in range(n):
            for j in range(m):
                if G[i][j] == 0:
                    G[i][j] = INF
        # special case for safe house.
        if G[n - 1][m - 1] != INF:
            G[n - 1][m - 1] += 1

        # for g in G:
        #     print(g)

        def OK(tx):
            dq = deque()
            visit = set()
            dq.append((0, 0, tx + 1))
            visit.add((0, 0))
            while dq:
                (i, j, t) = dq.popleft()
                if (i, j) == (n - 1, m - 1):
                    return True
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and G[x][y] != -1 and (G[x][y] > (t + 1)) and (x, y) not in visit:
                        # print(x, y, t + 1)
                        visit.add((x, y))
                        dq.append((x, y, t + 1))
            return False

        # print(OK(0))
        s, e = 0, n * m
        while s <= e:
            md = (s + e) // 2
            if OK(md):
                s = md + 1
            else:
                e = md - 1
        if e == n * m:
            e = INF
        return e


true, false, null = True, False, None
cases = [
    (
        [[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2],
         [0, 0, 0, 0, 0, 0, 0]],
        3),
    ([[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]], -1),
    ([[0, 0, 0], [2, 2, 0], [1, 2, 0]], 10 ** 9),
    ([[0, 2, 0, 0, 1], [0, 2, 0, 2, 2], [0, 2, 0, 0, 0], [0, 0, 2, 2, 0], [0, 0, 0, 0, 0]], 0),
    ([[0, 0, 0, 0, 0], [0, 2, 0, 2, 0], [0, 2, 0, 2, 0], [0, 2, 1, 2, 0], [0, 2, 2, 2, 0], [0, 0, 0, 0, 0]], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumMinutes, cases)

if __name__ == '__main__':
    pass
