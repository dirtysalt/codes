#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

# class Solution:
#     def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#         ans = []
#         for (left, right, k) in queries:
#             bk = [0] * 26
#             for c in s[left:right + 1]:
#                 bk[ord(c) - ord('a')] += 1
#             res = 0
#             for v in bk:
#                 if v % 2 != 0:
#                     res += 1
#             res = res // 2
#             ans.append(res <= k)
#         return ans


# class Solution:
#     def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#         bks = []
#         bk = [0] * 26
#         bks.append(bk)
#         for c in s:
#             bk = bk.copy()
#             bk[ord(c) - ord('a')] += 1
#             bks.append(bk)

#         ans = []
#         for (left, right, k) in queries:
#             left_bk = bks[left]
#             right_bk = bks[right + 1]
#             res = 0
#             for i in range(26):
#                 v = right_bk[i] - left_bk[i]
#                 if v % 2 != 0:
#                     res += 1
#             res = res // 2
#             ans.append(res <= k)
#         return ans

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        bks = [0] * (len(s) + 1)
        bk = 0
        for i, c in enumerate(s):
            bk = bk ^ (1 << (ord(c) - ord('a')))
            bks[i+1] = bk
            
        ans = []
        for (left, right, k) in queries:
            lbk = bks[left]
            rbk = bks[right + 1]
            v = rbk ^ lbk
            res = 0
            for i in range(26):
                if v & (1 << i):
                    res += 1
            res = res // 2
            ans.append(res <= k)
        return ans



import aatest_helper

true = True
false = False

cases = [
    ("abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2],
               [0, 4, 1]], [true, false, false, true, true])
]

aatest_helper.run_test_cases(Solution().canMakePaliQueries, cases)
