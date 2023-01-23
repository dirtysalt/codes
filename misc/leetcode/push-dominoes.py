#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#         n = len(dominoes)
#         if n == 0:
#             return ''

#         dp = [[None] * n, [None] * n]

#         st, t = '.', -1
#         for i in range(n):
#             if dominoes[i] == 'R':
#                 st, t = 'R', 0
#                 dp[0][i] = (st, t)
#             elif dominoes[i] == 'L':
#                 dp[0][i] = ('L', 0)
#                 st, t = '.', -1
#             else:
#                 dp[0][i] = (st, t + 1)
#                 t += 1

#         st, t = '.', -1
#         for i in reversed(range(n)):
#             if dominoes[i] == 'L':
#                 st, t = 'L', 0
#                 dp[1][i] = (st, t)
#             elif dominoes[i] == 'R':
#                 dp[1][i] = ('R', 0)
#                 st, t = '.', -1
#             else:
#                 dp[1][i] = (st, t + 1)
#                 t += 1

#         ans = [None] * n
#         for i in range(n):
#             l, lt = dp[0][i]
#             r, rt = dp[1][i]
#             if l != '.' and r != '.':
#                 if l == r:
#                     ans[i] = l
#                 elif lt < rt:
#                     ans[i] = l
#                 elif lt > rt:
#                     ans[i] = r
#                 else:
#                     ans[i] = '.'
#             elif l != '.':
#                 ans[i] = l
#             elif r != '.':
#                 ans[i] = r
#             else:
#                 ans[i] = '.'
#         ans = ''.join(ans)
#         return ans

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        if n == 0:
            return ''

        dp = [[None] * n, [None] * n]

        st, t = '.', -1
        for i in range(n):
            if dominoes[i] == 'R':
                st, t = 'R', 0
            elif dominoes[i] == 'L':
                st, t = '.', -1
            else:
                dp[0][i] = (st, t + 1)
                t += 1

        st, t = '.', -1
        for i in reversed(range(n)):
            if dominoes[i] == 'L':
                st, t = 'L', 0
            elif dominoes[i] == 'R':
                st, t = '.', -1
            else:
                dp[1][i] = (st, t + 1)
                t += 1

        ans = [None] * n
        for i in range(n):
            if dominoes[i] != '.':
                ans[i] = dominoes[i]
                continue

            l, lt = dp[0][i]
            r, rt = dp[1][i]
            if l != '.' and r != '.':
                if lt < rt:
                    ans[i] = l
                elif lt > rt:
                    ans[i] = r
                else:
                    ans[i] = '.'
            elif l != '.':
                ans[i] = l
            elif r != '.':
                ans[i] = r
            else:
                ans[i] = '.'
        ans = ''.join(ans)
        return ans


cases = [
    (".L.R...LR..L..", "LL.RR.LLRRLL.."),
    ("RR.L", "RR.L"),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().pushDominoes, cases)
