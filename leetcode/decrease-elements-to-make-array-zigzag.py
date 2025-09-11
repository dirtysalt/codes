#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def movesToMakeZigzag(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1: return 0
#
#         def fix(arr, odd):
#             ans = 0
#             for i in range(1, n):
#                 x, y = arr[i - 1], arr[i]
#                 if i % 2 == odd:
#                     if x >= y:
#                         # decrease a[i-1]. a[i-2] >= a[i-1] <= a[i]
#                         # 所以减掉应该是没有问题的.
#                         ans += (x - y) + 1
#                         arr[i - 1] = y - 1
#                 else:
#                     if x <= y:
#                         # decrease  a[i]
#                         ans += (y - x) + 1
#                         arr[i] = x - 1
#
#             # print(arr, ans)
#             return ans
#
#         ans = fix(nums[:], odd=0)
#         ans = min(ans, fix(nums[:], odd=1))
#         return ans

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        def fix(arr, odd):
            ans = 0
            pv = arr[0]
            for i in range(1, n):
                if i % 2 == odd:
                    if pv >= arr[i]:
                        # decrease a[i-1]. a[i-2] >= a[i-1] <= a[i]
                        # 所以减掉应该是没有问题的.
                        ans += (pv - arr[i] + 1)
                    pv = arr[i]
                else:
                    if pv <= arr[i]:
                        # decrease  a[i]
                        ans += (arr[i] - pv + 1)
                        pv = pv - 1
                    else:
                        pv = arr[i]
            # print(arr, ans)
            return ans

        ans = fix(nums, odd=0)
        ans = min(ans, fix(nums, odd=1))
        return ans


import aatest_helper

cases = [
    ([1, 2, 3], 2),
    ([9, 6, 1, 6, 2], 4),
    ([10, 4, 4, 10, 10, 6, 2, 3], 13),
    ([2, 7, 10, 9, 8, 9], 4)
]

aatest_helper.run_test_cases(Solution().movesToMakeZigzag, cases)
