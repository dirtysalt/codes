#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:

        from functools import cache

        n = len(words)

        @cache
        def search(a, b, i):
            if i == n:
                return 0

            w = words[i]
            # w + [a, b]
            c0 = len(w) + search(w[0], b, i + 1)
            if w[-1] == a:
                c0 -= 1

            # [a,b] + w
            c1 = len(w) + search(a, w[-1], i + 1)
            if w[0] == b:
                c1 -= 1

            return min(c0, c1)

        w = words[0]
        ans = search(w[0], w[-1], 1) + len(w)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (["aa", "ab", "bc"], 4),
    (["ab", "b"], 2),
    (["aaa", "c", "aba"], 6),
]

aatest_helper.run_test_cases(Solution().minimizeConcatenatedLength, cases)

if __name__ == '__main__':
    pass
