#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         n = len(A)
#         a = [A[i] + i for i in range(n)]
#         b = [A[i] - i for i in range(n)]
#         MAX_SIZE = 1000
#
#         def msort(a, b):
#             assert len(a) == len(b)
#             if len(a) == 1:
#                 return a, b
#
#             m = len(a) // 2
#             x, y = msort(a[:m], b[:m])
#             w, z = msort(a[m:], b[m:])
#
#             if len(a) >= MAX_SIZE and len(b) >= MAX_SIZE:
#                 return [], []
#
#             t0, t1 = merge(x, y, w, z)
#             return t0, t1
#
#         def merge(x, y, w, z):
#             # merge with x and z
#             self.ans = max(self.ans, x[-1] + z[-1])
#
#             # def f(a, b):
#             #     t = []
#             #     i, j = 0, 0
#             #     while i < len(a) and j < len(b):
#             #         if a[i] < b[j]:
#             #             t.append(a[i])
#             #             i += 1
#             #         else:
#             #             t.append(b[j])
#             #             j += 1
#             #     t.extend(a[i:])
#             #     t.extend(b[j:])
#             #     return t
#             #
#             # t0 = f(x, w)
#             # t1 = f(y, z)
#             # return t0, t1
#
#             # 直接用sorted比手写还要快
#             t0 = sorted(x + w)
#             t1 = sorted(y + z)
#             return t0, t1
#
#         self.ans = 0
#         msort(a, b)
#         return self.ans

# class Solution:
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         n = len(A)
#
#         a = [A[i] + i for i in range(n)]
#         b = [A[i] - i for i in range(n)]
#
#         for i in range(1, n):
#             a[i] = max(a[i], a[i - 1])
#
#         for i in reversed(range(n - 1)):
#             b[i] = max(b[i], b[i + 1])
#
#         ans = 0
#         for i in range(n - 1):
#             res = a[i] + b[i + 1]
#             ans = max(ans, res)
#         return ans


# class Solution:
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         n = len(A)
#
#         # a = [A[i] + i for i in range(n)]
#         b = [A[i] - i for i in range(n)]
#
#         # for i in range(1, n):
#         #     a[i] = max(a[i], a[i - 1])
#
#         for i in reversed(range(n - 1)):
#             b[i] = max(b[i], b[i + 1])
#
#         ans = 0
#         p = 0
#         for i in range(n - 1):
#             p = max(p, A[i] + i)
#             res = p + b[i + 1]
#             ans = max(ans, res)
#         return ans

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)

        ans = 0
        p = 0
        for i in range(1, n):
            # p always < i
            res = A[p] + p + A[i] - i
            ans = max(ans, res)
            if A[i] + i >= A[p] + p:
                p = i

        return ans


cases = [
    ([8, 1, 5, 2, 6], 11)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxScoreSightseeingPair, cases)
