#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         n = len(A)
#         ans = n
#         for x in range(1, 6 + 1):
#             a, b, c = 0, 0, 0
#             for i in range(n):
#                 if A[i] == x:
#                     a += 1
#                 if B[i] == x:
#                     b += 1
#                 if A[i] == x or B[i] == x:
#                     c += 1
#
#             if c == n:
#                 ans = min(ans, n - a, n - b)
#         if ans == n:
#             ans = -1
#         return ans


# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         n = len(A)
#         stat = [[0, 0, 0] for _ in range(7)]
#         ans = n
#
#         for i in range(n):
#             x = A[i]
#             stat[x][0] += 1
#             stat[x][2] += 1
#
#             x = B[i]
#             stat[x][1] += 1
#             stat[x][2] += 1
#
#             if A[i] == B[i]:
#                 stat[x][2] -= 1
#
#         for i in range(1, 7):
#             a, b, c = stat[i]
#             if c == n:
#                 ans = min(ans, c - a, c - b)
#
#         if ans == n:
#             ans = -1
#         return ans

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        ax = [0] * 7
        bx = [0] * 7
        cx = [0] * 7
        ans = n

        for i in range(n):
            x = A[i]
            ax[x] += 1
            cx[x] += 1

            x = B[i]
            bx[x] += 1
            cx[x] += 1

            if A[i] == B[i]:
                cx[x] -= 1

        for i in range(1, 7):
            if cx[i] == n:
                ans = min(ans, cx[i] - ax[i], cx[i] - bx[i])

        if ans == n:
            ans = -1
        return ans


cases = [
    ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
    ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDominoRotations, cases)
