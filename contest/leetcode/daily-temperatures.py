#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         n = len(T)
#         self.ans = [0] * n
#
#         def msort(a):
#             if len(a) == 1:
#                 return a
#             m = len(a) // 2
#             x = msort(a[:m])
#             y = msort(a[m:])
#             z = merge(x, y)
#             return z
#
#         def merge(x, y):
#             i, j = len(x) - 1, len(y) - 1
#             least_rigth_index = y[-1][1]
#             while i >= 0 and j >= 0:
#                 # print(i, j, x, y)
#                 if y[j][0] <= x[i][0]:
#                     i -= 1
#                     continue
#
#                 while j >= 0 and y[j][0] > x[i][0]:
#                     least_rigth_index = min(least_rigth_index, y[j][-1])
#                     j -= 1
#                 if self.ans[x[i][1]] == 0:
#                     self.ans[x[i][1]] = least_rigth_index
#                 i -= 1
#                 j += 1
#
#             return sorted(x + y)
#
#         tmp = [(T[i], i) for i in range(n)]
#         msort(tmp)
#         # print(self.ans)
#         ans = [max(self.ans[i] - i, 0) for i in range(n)]
#         return ans

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        right = []  # [(80, 9), (70, 6), (60, 4)..]
        ans = [0] * n

        # (value, index). value是逆序排列，而index則是順序排列
        def bs(v):
            s, e = 0, len(right) - 1
            while s <= e:
                m = (s + e) // 2
                if right[m][0] <= v:
                    e = m - 1
                else:
                    s = m + 1
            return right[e][1] if e >= 0 else -1

        for i in reversed(range(n)):
            # binary search it.
            # res = bs(T[i])
            # if res != -1:
            #     ans[i] = res - i

            # or linear search ??
            for (v, idx) in reversed(right):
                if v > T[i]:
                    ans[i] = idx - i
                    break

            while right and T[i] >= right[-1][0]:
                right.pop()
            right.append((T[i], i))

        return ans


cases = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().dailyTemperatures, cases)
