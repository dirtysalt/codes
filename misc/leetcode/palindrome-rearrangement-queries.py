#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        n2 = n // 2
        s1 = s[:n2]
        s2 = s[n2:][::-1]
        left = [0] * n2
        right = [0] * n2
        for i in range(0, n2):
            left[i] = (s1[i] == s2[i]) & (left[i - 1] if i > 0 else 1)
        for i in reversed(range(n2)):
            right[i] = (s1[i] == s2[i]) & (right[i + 1] if (i + 1) < n2 else 1)

        acc1 = [[0] * 26 for _ in range(n2 + 1)]
        acc2 = [[0] * 26 for _ in range(n2 + 1)]
        for i in range(n2):
            for j in range(26):
                acc1[i + 1][j] = acc1[i][j]
                acc2[i + 1][j] = acc2[i][j]
            d = ord(s1[i]) - ord('a')
            acc1[i + 1][d] += 1
            d = ord(s2[i]) - ord('a')
            acc2[i + 1][d] += 1

        def get_range(acc, l, r):
            A = [0] * 26
            for j in range(26):
                A[j] = acc[r + 1][j] - acc[l][j]
            return A

        def check_range(l, r):
            A = get_range(acc1, l, r)
            B = get_range(acc2, l, r)
            return A == B

        def check_identity(l, r):
            if l > r: return True
            return s1[l:r + 1] == s2[l:r + 1]

        def handle(a, b, c, d):
            c, d = n - 1 - d, n - c - 1
            # print(a, b, c, d)
            l, r = min(a, c), max(b, d)
            if l > 0 and not left[l - 1]: return False
            if (r + 1) < n2 and not right[r + 1]: return False

            # print("'%s' '%s' '%s'" % (s1[:a], s1[a:b + 1], s1[b + 1:]) +
            #       "-> '%s' '%s' '%s'" % (s2[:c], s2[c:d + 1], s2[d + 1:]))

            # if one range is larger.
            if (a >= c and b <= d) or (a <= c and b >= d):
                return check_range(l, r)

            # if ranges not overlapped.
            if b < c or d < a:
                if not check_range(a, b) or not check_range(c, d):
                    return False
                return check_identity(b + 1, c - 1) and check_identity(d + 1, a - 1)

            # ranges are overlapped.
            ax, ay = acc1, acc2
            if a > c:
                a, b, c, d = c, d, a, b
                ax, ay = ay, ax
            A = get_range(ax, a, b)
            B = get_range(ay, c, d)

            C = get_range(ay, a, c - 1)
            for j in range(26):
                if A[j] < C[j]: return False
                A[j] -= C[j]
            C = get_range(ax, b + 1, d)
            for j in range(26):
                if B[j] < C[j]: return False
                B[j] -= C[j]
            return A == B

        ans = []
        for (a, b, c, d) in queries:
            r = handle(a, b, c, d)
            ans.append(r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(s="abcabc", queries=[[1, 1, 3, 5], [0, 2, 5, 5]], res=[true, true]),
    aatest_helper.OrderedDict(s="abbcdecbba", queries=[[0, 2, 7, 9]], res=[false]),
    aatest_helper.OrderedDict(s="acbcab", queries=[[1, 2, 4, 5]], res=[true]),
    ("odaxusaweuasuoeudxwa", [[0, 5, 10, 14]], [false]),
]

aatest_helper.run_test_cases(Solution().canMakePalindromeQueries, cases)

if __name__ == '__main__':
    pass
