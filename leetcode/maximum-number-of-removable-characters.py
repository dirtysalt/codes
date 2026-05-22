#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def test(sz):
            rem = set(removable[:sz])
            CS = [0] * 26
            for i in range(len(s)):
                if i in rem: continue
                c = s[i]
                CS[ord(c) - ord('a')] += 1
            for c in p:
                CS[ord(c) - ord('a')] -= 1

            for i in range(26):
                if CS[i] < 0: return False

            j = 0
            for i in range(len(s)):
                if j == len(p): break
                if i in rem: continue

                c = ord(s[i]) - ord('a')
                CS[c] -= 1
                if s[i] == p[j]:
                    CS[ord(p[j]) - ord('a')] += 1
                    j += 1
                if CS[c] < 0: return False

            return True

        L, U = 0, len(removable)
        while L <= U:
            sz = (L + U) // 2
            if test(sz):
                L = sz + 1
            else:
                U = sz - 1
        ans = U
        return ans


true, false, null = True, False, None
cases = [
    ("abcacb", "ab", [3, 1, 0], 2),
    ("abcbddddd", "abcd", [3, 2, 1, 4, 5, 6], 1),
    ("abcab", "abc", [0, 1, 2, 3, 4], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumRemovals, cases)

if __name__ == '__main__':
    pass
