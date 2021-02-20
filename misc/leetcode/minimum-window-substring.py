#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         from collections import Counter
#         tc = Counter()
#         for x in t:
#             tc[x] += 1
#
#         def overlap(xs, ys):
#             for k in ys:
#                 if xs[k] < ys[k]:
#                     return False
#             return True
#
#         j = 0
#         sc = Counter()
#         res = None
#         res_sz = len(s) + 1
#         for i, x in enumerate(s):
#             sc[x] += 1
#             if overlap(sc, tc):
#                 while j <= i and overlap(sc, tc):
#                     sc[s[j]] -= 1
#                     j += 1
#                 # consider j-1, i
#                 if (i - j + 2) < res_sz:
#                     res_sz = (i - j + 2)
#                     res = (j - 1, i)
#
#         if res is None:
#             return ""
#         (x, y) = res
#         ans = s[x: y + 1]
#         return ans


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        tc = Counter()
        for x in t:
            tc[x] += 1

        j = 0
        sc = Counter()
        res = None
        res_sz = len(s) + 1
        cover = 0
        for i, x in enumerate(s):
            sc[x] += 1
            if sc[x] == tc[x]:
                cover += 1

            if cover == len(tc):
                while j <= i and cover == len(tc):
                    if sc[s[j]] == tc[s[j]]:
                        cover -= 1
                    sc[s[j]] -= 1
                    j += 1
                # consider j-1, i
                if (i - j + 2) < res_sz:
                    res_sz = (i - j + 2)
                    res = (j - 1, i)

        if res is None:
            return ""
        (x, y) = res
        ans = s[x: y + 1]
        return ans


cases = [
    ('ADOBECODEBANC', 'ABC', "BANC"),
    ("bba", "ab", "ba"),
    ("aa", "aa", "aa"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minWindow, cases)
