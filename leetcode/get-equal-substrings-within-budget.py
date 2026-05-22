#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         n = len(s)
#         ans = 0
#
#         def bs(a, x):
#             s, e = 0, len(a) - 1
#             while s <= e:
#                 m = (s + e) // 2
#                 if a[m] < x:
#                     s = m + 1
#                 else:
#                     e = m - 1
#             return e
#
#         costs = [0]
#         for i in range(n):
#             c = abs(ord(s[i]) - ord(t[i]))
#             costs.append(costs[-1] + c)
#
#         print(costs)
#         for i in range(1, len(costs)):
#             v = costs[i]
#             target = v - maxCost
#             idx = bs(costs, target)
#             res = i - 1 - idx
#             ans = max(res, ans)
#         return ans

# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         n = len(s)
#         ans = 0
#
#         costs = []
#         for i in range(n):
#             c = abs(ord(s[i]) - ord(t[i]))
#             costs.append(c)
#
#         j, res = 0, 0
#         for i in range(n):
#             res += costs[i]
#             while j <= i and res > maxCost:
#                 res -= costs[j]
#                 j += 1
#             ans = max(ans, (i - j) + 1)
#         return ans

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans = 0

        j, res = 0, 0
        for i in range(n):
            c = abs(ord(s[i]) - ord(t[i]))
            res += c
            while j <= i and res > maxCost:
                res -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            ans = max(ans, (i - j) + 1)
        return ans


import aatest_helper

cases = [
    ('abcd', 'bcdf', 3, 3),
    ("krrgw", "zjxss", 19, 2),
    ("abcd", "bcdf", 200, 4)
]

aatest_helper.run_test_cases(Solution().equalSubstring, cases)
