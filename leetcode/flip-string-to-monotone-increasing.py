#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def minFlipsMonoIncr(self, S: str) -> int:
#
#         # tmp0[i], S[0..i] 有多少个0
#         # tmp1[i], S[i..] 有多少个0
#         tmp0 = [0] * len(S)
#         tmp1 = [0] * len(S)
#
#         res = 0
#         for i in range(len(S)):
#             c = S[i]
#             if c == '0':
#                 res += 1
#             tmp0[i] = res
#
#         res = 0
#         for i in reversed(range(len(S))):
#             c = S[i]
#             if c == '0':
#                 res += 1
#             tmp1[i] = res
#
#         # change to 000111
#         ans = len(S)
#         for i in range(len(S)):
#             c = S[i]
#             l, r = tmp0[i - 1] if i > 0 else 0, tmp1[i + 1] if (i + 1) < len(S) else 0
#             a = (i - l) + r
#             # b = l + (len(S) - i - 1)
#             # ans = min(ans, a, b)
#             ans = min(ans, a)
#         return ans
#

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        ans = len(S)

        c1 = 0
        for c in S:
            if c == '1':
                c1 += 1

        c0 = 0
        for i in range(len(S)):
            c = S[i]
            if c == '1':
                c1 -= 1

            # i 左边有c0个0, 右边c1个1.
            a = (i - c0) + (len(S) - i - 1 - c1)
            ans = min(a, ans)

            if c == '0':
                c0 += 1
        return ans


cases = [
    ("00110", 1),
    ("010110", 2),
    ("00011000", 2),
    ("0101100011", 3),
    ("1111001110", 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minFlipsMonoIncr, cases)
