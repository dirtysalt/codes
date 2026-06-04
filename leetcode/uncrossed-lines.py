#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
#         n = len(A)
#         m = len(B)
#         cache = {}
#
#         def test(i, j):
#             if i == n or j == m:
#                 return 0
#
#             key = '{}.{}'.format(i, j)
#             if key in cache:
#                 return cache[key]
#
#             res = 0
#             while i < n and j < m and A[i] == B[j]:
#                 i += 1
#                 j += 1
#                 res += 1
#
#             if i == n or j == m:
#                 cache[key] = res
#                 return res
#
#             a = test(i + 1, j)
#             b = test(i, j + 1)
#             res += max(a, b)
#             cache[key] = res
#
#             return res
#
#         ans = test(0, 0)
#         return ans
#
# class Solution:
#     def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
#         n = len(A)
#         m = len(B)
#         dp = [[0] * (m + 1) for _ in range(n + 1)]
#
#         for i in range(n):
#             for j in range(m):
#                 dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (1 if A[i] == B[j] else 0))
#
#         ans = dp[n][m]
#         return ans


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # note(yan): discusson里面提到的优化点，只保留AB两个的交集
        commons = set(A) & set(B)
        A = [x for x in A if x in commons]
        B = [x for x in B if x in commons]

        n = len(A)
        m = len(B)
        dp = [[0] * (m + 1), [0] * (m + 1)]
        now = 0

        for i in range(n):
            for j in range(m):
                dp[1 - now][j + 1] = max(dp[now][j + 1], dp[1 - now][j], dp[now][j] + (1 if A[i] == B[j] else 0))
            now = 1 - now

        ans = dp[now][m]
        return ans


cases = [
    ([1, 4, 2], [1, 2, 4], 2),
    ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
    ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ([2, 1], [1, 2, 1, 3, 3, 2], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxUncrossedLines, cases)
