#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
#         n = len(books)
#         inf = 1 << 30
#         dp = [inf] * (n + 1)
#         dp[0] = 0
#
#         for i in range(1, n + 1):
#             w = 0
#             h = 0
#             for j in range(i - 1, n):
#                 w += books[j][0]
#                 h = max(h, books[j][1])
#                 if w > shelf_width:
#                     break
#                 dp[j + 1] = min(dp[j + 1], dp[i - 1] + h)
#
#         ans = dp[n]
#         return ans

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        """python里面这种a[-1]很有意思"""
        n = len(books)
        inf = 1 << 30
        dp = [inf] * (n + 1)
        dp[-1] = 0

        for i in range(n):
            w = 0
            h = 0
            for j in range(i, n):
                w += books[j][0]
                h = max(h, books[j][1])
                if w > shelf_width:
                    break
                dp[j] = min(dp[j], dp[i - 1] + h)

        ans = dp[n - 1]
        return ans


cases = [
    ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4, 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minHeightShelves, cases)
