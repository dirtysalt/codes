#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

#
#
# class Tree:
#     def __init__(self, s, e):
#         self.s = s
#         self.e = e
#         self.left = None
#         self.right = None
#         self.val = 0
#
#
# def build_tree(s, e):
#     if s == e:
#         return Tree(s, e)
#     m = (s + e) // 2
#     t1 = build_tree(s, m)
#     t2 = build_tree(m + 1, e)
#     t = Tree(s, e)
#     t.left = t1
#     t.right = t2
#     return t
#
#
# def update_tree(t, s, e, v):
#     if t.s == s and t.e == e:
#         t.val += v
#         return
#
#     m = (t.s + t.e) // 2
#     # [t.s .. m]
#     if t.s <= s <= m:
#         update_tree(t.left, s, min(m, e), v)
#     # [m+1.. t.e]
#     if (m + 1) <= e <= t.e:
#         update_tree(t.right, max(m + 1, s), e, v)
#
#     return
#
#
# def walk_tree(t, ans, pfx):
#     if t.s == t.e:
#         ans.append(pfx + t.val)
#         return
#
#     pfx += t.val
#     walk_tree(t.left, ans, pfx)
#     walk_tree(t.right, ans, pfx)
#     return
#
#
# class Solution:
#     def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
#         t = build_tree(1, n)
#         for i, j, k in bookings:
#             update_tree(t, i, j, k)
#         ans = []
#         walk_tree(t, ans, 0)
#         return ans


# class Solution:
#     def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
#         eva = [(x[0], x[2]) for x in bookings]
#         evb = [(x[1], x[2]) for x in bookings]
#
#         eva.sort()
#         evb.sort()
#
#         ans = []
#         res = 0
#         pa, pb = 0, 0
#         for i in range(1, n + 1):
#             while pa < len(eva) and eva[pa][0] == i:
#                 res += eva[pa][1]
#                 pa += 1
#             ans.append(res)
#
#             while pb < len(evb) and evb[pb][0] == i:
#                 res -= evb[pb][1]
#                 pb += 1
#
#             if pb == len(evb):
#                 ans.extend([res] * (n - i))
#                 break
#
#         return ans

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        tmp = [0] * (n + 2)

        for i, j, k in bookings:
            tmp[i] += k
            tmp[j + 1] -= k

        ans = []
        res = 0
        for i in range(1, n + 1):
            res += tmp[i]
            ans.append(res)

        return ans


cases = [
    ([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5, [10, 55, 45, 25, 25])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().corpFlightBookings, cases)
