#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         s = [ord(c) - ord('a') for c in s]
#         p = [ord(c) - ord('a') for c in p]
#
#         pv = [0] * 26
#         for c in p:
#             pv[c] += 1
#
#         sv = [0] * 26
#
#         def contains(a, b):
#             for i in range(len(a)):
#                 if a[i] < b[i]:
#                     return False
#             return True
#
#         j = 0
#         ans = []
#         for i in range(len(s)):
#             sv[s[i]] += 1
#
#             if contains(sv, pv):
#                 while j <= i and contains(sv, pv):
#                     sv[s[j]] -= 1
#                     j += 1
#                 # [j-1..i]. size = (i-j+2)
#                 if (i - j + 2) == len(p):
#                     ans.append(j - 1)
#
#         return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s = [ord(c) - ord('a') for c in s]
        p = [ord(c) - ord('a') for c in p]

        pv = [0] * 26
        for c in p:
            pv[c] += 1

        sv = [0] * 26
        j = 0
        ans = []
        for i in range(len(s)):
            sv[s[i]] += 1

            if (i - j + 1) == len(p):
                if sv == pv:
                    ans.append(j)
                sv[s[j]] -= 1
                j += 1
        return ans


cases = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("abaacbabc", "abc", [3, 4, 6])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findAnagrams, cases)
