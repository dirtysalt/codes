#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
#         n = len(customers)
#
#         acc = customers.copy()
#         for i in range(1, n):
#             acc[i] += acc[i - 1]
#
#         left = [0] * n
#         right = [0] * n
#         res = 0
#         for i in range(n):
#             if grumpy[i] == 0:
#                 res += customers[i]
#             left[i] = res
#         res = 0
#         for i in reversed(range(n)):
#             if grumpy[i] == 0:
#                 res += customers[i]
#             right[i] = res
#
#         ans = 0
#         for i in range(n):
#             # left[0..i-1], right[i+X..], acc[i+X-1] - acc[i-1]
#             a = left[i - 1] if i >= 1 else 0
#             b = right[i + X] if (i + X) < n else 0
#             c = acc[i + X - 1] if (i + X - 1) < n else acc[-1]
#             d = acc[i - 1] if i >= 1 else 0
#             res = (a + b + c - d)
#             # print(i, a, b, c - d, res)
#             ans = max(res, ans)
#         return ans
#

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        if X >= n:
            return sum(customers)

        arr = [customers[i] if grumpy[i] == 0 else 0 for i in range(n)]

        a, b, c = 0, 0, 0
        for i in range(X):
            b += customers[i]
        for i in range(X, n):
            c += arr[i]

        # print(a, b, c)
        ans = a + b + c
        for i in range(X, n):
            j = i - X
            a += arr[j]
            c -= arr[i]
            b = b - customers[j] + customers[i]
            # print(i, a, b, c)
            ans = max(ans, a + b + c)
        return ans


cases = [
    ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16),
    # ([1, 0, 1, 2, 1, 1, 7, 5, 8], [0, 1, 0, 1, 0, 1, 0, 0, 1], 3, 16),

]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxSatisfied, cases)
