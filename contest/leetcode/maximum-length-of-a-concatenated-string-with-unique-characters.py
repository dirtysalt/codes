#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         n = len(arr)
#         mask = [0] * 26
#
#         def is_ok():
#             for v in mask:
#                 if v > 1:
#                     return False
#             return True
#
#         j = 0
#         ans = 0
#         for i in range(n):
#             s = arr[i]
#             for c in s:
#                 v = ord(c) - ord('a')
#                 mask[v] += 1
#
#             while not is_ok():
#                 for c in arr[j]:
#                     v = ord(c) - ord('a')
#                     mask[v] -= 1
#                 j += 1
#
#             res = 0
#             for k in range(j, i + 1):
#                 res += len(arr[k])
#             ans = max(ans, res)
#
#         return ans

# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         def is_self_conflict(a):
#             mask = [0] * 26
#             for c in a:
#                 v = ord(c) - ord('a')
#                 if mask[v] != 0:
#                     return True
#                 mask[v] = 1
#             return False
#
#         arr = [x for x in arr if not is_self_conflict(x)]
#         n = len(arr)
#
#         def is_conflict(a, b):
#             return True if (set(a) & set(b)) else False
#
#         mat = [[False] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if is_conflict(arr[i], arr[j]):
#                     mat[i][j] = True
#                     mat[j][i] = True
#
#         # print(mat)
#         ans = 0
#         for i in reversed(range(1 << n)):
#             xs = [x for x in range(n) if (i >> x) & 0x1]
#             res = sum([len(arr[x]) for x in xs])
#             if res <= ans:
#                 continue
#
#             ok = True
#             for j in range(len(xs)):
#                 for k in range(j + 1, len(xs)):
#                     if mat[xs[j]][xs[k]]:
#                         ok = False
#                         break
#                 if not ok: break
#             if ok:
#                 ans = res
#         return ans

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for x in arr:
            xs = set(x)
            if len(xs) != len(x):
                continue

            for ys in dp[:]:
                if xs & ys:
                    continue
                dp.append(xs | ys)

        return max(len(xs) for xs in dp)


cases = [
    (["cha", "r", "act", "ers"], 6),
    (["un", "iq", "ue"], 4),
    (["abcdefghijklmnopqrstuvwxyz"], 26),
    (["ab", "ba", "cd", "dc", "ef", "fe", "gh", "hg", "ij", "ji", "kl", "lk", "mn", "nm", "op", "po"], 16),
    (["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"], 11)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxLength, cases)
