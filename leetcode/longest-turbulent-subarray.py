#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# case0. For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# case1. OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.

# class Solution:
#     def maxTurbulenceSize(self, A: List[int]) -> int:
#         n = len(A)
#         dp = [[0] * n, [0] * n]
#         dp[0][0] = 1
#         dp[1][0] = 1
#
#         for k in range(0, n - 1):
#             if A[k] == A[k + 1]:
#                 dp[0][k + 1] = 1
#                 dp[1][k + 1] = 1
#                 continue
#
#             if k % 2 == 1:
#                 # case 0 ok, case 1 failed.
#                 if A[k] > A[k + 1]:
#                     dp[0][k + 1] = max(dp[0][k] + 1, 2)
#                     dp[1][k + 1] = 1
#                 else:
#                     dp[1][k + 1] = max(dp[1][k] + 1, 2)
#                     dp[0][k + 1] = 1
#             elif k % 2 == 0:
#                 # case 0 ok, case 1failed.
#                 if A[k] < A[k + 1]:
#                     dp[0][k + 1] = max(dp[0][k] + 1, 2)
#                     dp[1][k + 1] = 1
#                 else:
#                     dp[1][k + 1] = max(dp[1][k] + 1, 2)
#                     dp[0][k + 1] = 1
#
#         ans = 1
#         ans = max(max(dp[0]), ans)
#         ans = max(max(dp[1]), ans)
#         return ans
#

# class Solution:
#     def maxTurbulenceSize(self, A: List[int]) -> int:
#         n = len(A)
#
#         def test(odd):
#             ans = 1
#             res = 1
#             for i in range(1, n):
#                 ans = max(ans, res)
#                 if A[i] == A[i - 1]:
#                     res = 1
#                     continue
#
#                 if i % 2 == odd:
#                     if A[i - 1] > A[i]:
#                         res += 1
#                     else:
#                         res = 2
#                         odd = 1 - odd
#
#                 else:
#                     if A[i - 1] < A[i]:
#                         res += 1
#                     else:
#                         res = 2
#                         odd = 1 - odd
#             ans = max(ans, res)
#             return ans
#
#         ans = 1
#         ans = max(test(0), ans)
#         # 只需要测试一个方向即可，因为如果第一个元素不满足条件的话就立刻做调整
#         # ans = max(test(1), ans)
#         return ans

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)

        odd = 0
        ans = 1
        res = 1
        for i in range(1, n):
            if A[i] == A[i - 1]:
                res = 1
                continue
            b1 = i & 0x1
            if ((b1 == odd) and A[i - 1] > A[i]) or ((b1 == (1 - odd)) and A[i - 1] < A[i]):
                res += 1
            else:
                res = 2
                odd = 1 - odd
            ans = max(ans, res)
        return ans


cases = [
    ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
    ([4, 8, 12, 16], 2),
    ([100], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxTurbulenceSize, cases)
