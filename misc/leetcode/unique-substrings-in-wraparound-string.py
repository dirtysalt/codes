#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def findSubstringInWraproundString(self, p: str) -> int:
#         n = len(p)
#         if n == 0:
#             return 0
#         ans = 0
#         from collections import defaultdict
#         cache = defaultdict(int)
#
#         def is_consective(a, b):
#             a = ord(a) - ord('a')
#             b = ord(b) - ord('a')
#             return (a + 1) % 26 == b
#
#         sz = 1
#         cache[p[0]] = sz
#         for i in range(1, n):
#             a, b = p[i - 1], p[i]
#             if is_consective(a, b):
#                 sz += 1
#             else:
#                 sz = 1
#             cache[b] = max(cache[b], sz)
#
#         # print(cache)
#         for c, sz in cache.items():
#             ans += sz
#         return ans

# 思路是：对于当前字符b, 更新以这个字符b结尾的最大长度 sz
# 那么以字符b结尾的话，可以构造出不重复的 sz 个字符串
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        if n == 0:
            return 0
        p = [ord(x) - ord('a') for x in p]

        ans = 0
        cache = [0] * 26

        sz = 1
        cache[p[0]] = sz

        for i in range(1, n):
            a, b = p[i - 1], p[i]
            if (a + 1) % 26 == b:
                sz += 1
            else:
                sz = 1
            cache[b] = max(cache[b], sz)

        for sz in cache:
            ans += sz
        return ans


cases = [
    ("zab", 6),
    ("cac", 2),
    ("a", 1),
    ("abcabc", 6),
    ("zaba", 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findSubstringInWraproundString, cases)
