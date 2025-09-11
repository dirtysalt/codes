#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        row_edge = [(m, -1)] * n
        col_edge = [(n, -1)] * m
        row_set = set()
        col_set = set()

        def clear():
            row_edge.clear()
            row_edge.extend([(m, -1)] * n)
            col_edge.clear()
            col_edge.extend([(n, -1)] * m)
            row_set.clear()
            col_set.clear()

        def update(i, j):
            row_edge[i] = (min(row_edge[i][0], j), max(row_edge[i][1], j))
            col_edge[j] = (min(col_edge[j][0], i), max(col_edge[j][1], i))

        def dfs(i, j):
            row_set.add(i)
            col_set.add(j)
            visited.add((i, j))
            update(i, j)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 0 and (x, y) not in visited:
                    dfs(x, y)

        def check():
            for r in row_set:
                (c0, c1) = row_edge[r]
                if (c0 - 1) >= 0 and grid[r][c0 - 1] == 1 and (c1 + 1) < m and grid[r][c1 + 1] == 1:
                    continue
                # print('R', r, c0, c1)
                return 0
            for c in col_set:
                (r0, r1) = col_edge[c]
                if (r0 - 1) >= 0 and grid[r0 - 1][c] == 1 and (r1 + 1) < n and grid[r1 + 1][c] == 1:
                    continue
                # print('C', c, r0, r1)
                return 0
            return 1

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in visited:
                    clear()
                    dfs(i, j)
                    ans += check()
        return ans


cases = [
    ([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0]], 2),
    ([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]], 1),
    ([[1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1]], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().closedIsland, cases)
