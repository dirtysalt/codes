#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def hasValidPath(self, grid: List[List[int]]) -> bool:
#         pixels = [
#             [0, 0, 0, 1, 1, 1, 0, 0, 0],
#             [0, 1, 0, 0, 1, 0, 0, 1, 0],
#             [0, 0, 0, 1, 1, 0, 0, 1, 0],
#             [0, 0, 0, 0, 1, 1, 0, 1, 0],
#             [0, 1, 0, 1, 1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 1, 1, 0, 0, 0]
#         ]
#
#         n, m = len(grid), len(grid[0])
#         mat = [[0] * 3 * m for _ in range(3 * n)]
#
#         for i in range(n):
#             for j in range(m):
#                 x = grid[i][j] - 1
#                 mat[3 * i][3 * j:3 * j + 3] = pixels[x][:3]
#                 mat[3 * i + 1][3 * j:3 * j + 3] = pixels[x][3:6]
#                 mat[3 * i + 2][3 * j:3 * j + 3] = pixels[x][6:]
#
#         visited = set()
#         n = 3 * n
#         m = 3 * m
#         path = []
#
#         def dfs():
#             while path:
#                 (i, j) = path.pop()
#                 visited.add((i, j))
#                 for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#                     x, y = i + dx, j + dy
#                     if (x, y) == (n - 2, m - 2):
#                         return True
#                     if 0 <= x < n and 0 <= y < m and mat[x][y] == 1 and (x, y) not in visited:
#                         path.append((x, y))
#             return False
#
#         # for x in mat:
#         #     print(x)
#
#         path.append((1, 1))
#         ans = dfs()
#         return ans

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        out_dirs = [
            '', 'LR', 'UD', 'DL', 'DR', 'LU', 'UR'
        ]
        in_dirs = [
            '', 'LR', 'UD', 'UR', 'LU', 'RD', 'DL'
        ]
        dxy = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)
        }

        n, m = len(grid), len(grid[0])
        visited = set()
        path = []

        def dfs():
            while path:
                (i, j) = path.pop()
                # print(i, j)
                visited.add((i, j))
                if (i, j) == (n - 1, m - 1):
                    return True
                for d in out_dirs[grid[i][j]]:
                    dx, dy = dxy[d]
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                        if d not in in_dirs[grid[x][y]]:
                            continue
                        path.append((x, y))
            return False

        # for x in mat:
        #     print(x)

        path.append((0, 0))
        ans = dfs()
        return ans


cases = [
    ([[1, 2, 1], [1, 2, 1]], False),
    ([[2], [2], [2], [2], [2], [2], [6]], True),
    ([[1, 1, 1, 1, 1, 1, 3]], True),
    ([[2, 4, 3], [6, 5, 2]], True),
    ([[1, 1, 2]], False),
    ([[4, 1], [6, 1]], True),
    ([[6, 1, 3], [4, 1, 5]], True),
    ([[1]], True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().hasValidPath, cases)
