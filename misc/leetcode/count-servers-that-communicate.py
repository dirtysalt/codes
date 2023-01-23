#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#
#         ans = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     a = grid[i - 1][j] if i > 0 else 0
#                     b = grid[i][j - 1] if j > 0 else 0
#                     if a >= 1 or b >= 1:
#                         grid[i][j] = 2
#                         if i > 0 and grid[i - 1][j] == 1:
#                             grid[i - 1][j] = 2
#                         if j > 0 and grid[i][j - 1] == 1:
#                             grid[i][j - 1] = 2
#
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 2:
#                     ans += 1
#         return ans


# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#
#         ans = set()
#         for i in range(n):
#
#             c = 0
#             for j in range(m):
#                 if grid[i][j] > 0:
#                     c += 1
#             if c < 2:
#                 continue
#             for j in range(m):
#                 if grid[i][j] > 0:
#                     ans.add((i, j))
#
#         for j in range(m):
#             c = 0
#             for i in range(n):
#                 if grid[i][j] > 0:
#                     c += 1
#             if c < 2:
#                 continue
#             for i in range(n):
#                 if grid[i][j] > 0:
#                     ans.add((i, j))
#
#         ans = len(ans)
#         return ans
#

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        ans = set()
        for i in range(n):

            c = 0
            for j in range(m):
                if grid[i][j] > 0:
                    c += 1
                    if c >= 2:
                        break

            if c < 2:
                continue
            for j in range(m):
                if grid[i][j] > 0:
                    ans.add((i, j))

        for j in range(m):
            c = 0
            for i in range(n):
                if grid[i][j] > 0:
                    c += 1
                    if c >= 2:
                        break
            if c < 2:
                continue
            for i in range(n):
                if grid[i][j] > 0:
                    ans.add((i, j))

        ans = len(ans)
        return ans


cases = [
    ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
    ([[1, 0], [1, 1]], 3),
    ([[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countServers, cases)
