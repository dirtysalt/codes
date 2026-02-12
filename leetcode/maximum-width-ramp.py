#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def maxWidthRamp(self, A: List[int]) -> int:
#         n = len(A)
#         tmp = [(A[-1], n - 1)]
#
#         def bs(v, p):
#             # 如果v是最大值的话，那么在最后插入
#             if v > tmp[-1][0]:
#                 tmp.append((v, p))
#                 return p
#
#             s, e = 0, len(tmp) - 1
#             while s <= e:
#                 m = (s + e) // 2
#                 if tmp[m][0] == v:
#                     return tmp[m][1]
#                 if tmp[m][0] < v:
#                     s = m + 1
#                 else:
#                     e = m - 1
#
#             j = s
#             # 否则在j点插入. s[..j-1] + (s[j] = v) + s[j..]
#             pos = tmp[j][1]
#             tmp.insert(j, (v, pos))
#             return pos
#
#         ans = 0
#         for i in reversed(range(n - 1)):
#             p = bs(A[i], i)
#             # print(i, p, A[i], tmp)
#             ans = max(ans, p - i)
#         return ans

# class Solution:
#     def maxWidthRamp(self, A: List[int]) -> int:
#         n = len(A)
#         tmp = [(A[i], i) for i in range(n)]
#         tmp.sort()
#
#         p = tmp[-1][1]
#         for i in reversed(range(n - 1)):
#             if tmp[i][1] < p:
#                 tmp[i] = (tmp[i][0], p)
#             else:
#                 p = tmp[i][1]
#
#         def bs(v):
#             s, e = 0, n - 1
#             while s <= e:
#                 m = (s + e) // 2
#                 if tmp[m][0] == v:
#                     return tmp[m][1]
#                 if tmp[m][0] < v:
#                     s = m + 1
#                 else:
#                     e = m - 1
#             return tmp[s][1]
#
#         ans = 0
#         for i in reversed(range(n - 1)):
#             p = bs(A[i])
#             # print(i, p, A[i], tmp)
#             ans = max(ans, p - i)
#         return ans
#
# class Solution:
#     def maxWidthRamp(self, A: List[int]) -> int:
#         n = len(A)
#         tmp = [(A[i], i, i) for i in range(n)]
#         tmp.sort()
#
#         p = tmp[-1][1]
#         for i in reversed(range(n - 1)):
#             if tmp[i][1] < p:
#                 tmp[i] = (tmp[i][0], p, tmp[i][2])
#             else:
#                 p = tmp[i][1]
#         # print(tmp)
#         ans = 0
#         for i in range(n):
#             ans = max(ans, tmp[i][1] - tmp[i][2])
#         return ans
#

# class Solution:
#     def maxWidthRamp(self, A: List[int]) -> int:
#         n = len(A)
#         tmp = [(A[i], i) for i in range(n)]
#         tmp.sort()
#
#         ans = 0
#         p = tmp[-1][1]
#         for i in reversed(range(n - 1)):
#             if tmp[i][1] < p:
#                 ans = max(ans, p - tmp[i][1])
#             else:
#                 p = tmp[i][1]
#         return ans


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        tmp = list(range(n))
        tmp.sort(key=lambda x: A[x])

        ans = 0
        p = tmp[-1]
        for i in reversed(range(n - 1)):
            if tmp[i] < p:
                ans = max(ans, p - tmp[i])
            else:
                p = tmp[i]
        return ans


cases = [
    ([6, 0, 8, 2, 1, 5], 4),
    ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxWidthRamp, cases)
