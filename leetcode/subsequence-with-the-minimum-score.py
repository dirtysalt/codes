#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect
import functools
from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        left = [0] * m
        right = [0] * m
        INF = 10 ** 9
        ans = m

        i = 0
        for j in range(m):
            while i < n and s[i] != t[j]:
                i += 1
            left[j] = i
            if i < n:
                ans = min(ans, m - 1 - j)
                i += 1

        i = n - 1
        for j in reversed(range(m)):
            while i >= 0 and s[i] != t[j]:
                i -= 1
            right[j] = i
            if i >= 0:
                ans = min(ans, j)
                i -= 1

        # print(left, right, ans)
        j2 = 0
        for j in range(m):
            p = left[j]
            if p == n: break
            j2 = max(j2, j + 1)
            while j2 < m and right[j2] <= p:
                j2 += 1
            d = j2 - j - 1
            ans = min(ans, d)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("abacaba", "bzaa", 1),
    ("cde", "xyz", 3),
    ("abecdebe", "eaebceae", 6),
    ("acdedcdbabecdbebda", "bbecddb", 1),
    ("adebddaccdcabaade", "adbae", 0),
]

aatest_helper.run_test_cases(Solution().minimumScore, cases)

if __name__ == '__main__':
    pass
