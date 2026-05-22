#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        from functools import cache
        # AA 0
        # BB 1
        # AB 2
        matches = [
            [1],  # AABB
            [0, 2],  # BBAB, BBAB
            [0, 2],  # ABAA, ABAB
            [0, 1, 2]
        ]

        @cache
        def search(last, rest):
            ans = 0

            for x in matches[last]:
                if rest[x] > 0:
                    r = list(rest)
                    r[x] -= 1
                    c = search(x, tuple(r)) + 2
                    ans = max(ans, c)

            return ans

        ans = search(-1, (x, y, z))
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (2, 5, 1, 12),
    (3, 2, 2, 14),
]

aatest_helper.run_test_cases(Solution().longestString, cases)

if __name__ == '__main__':
    pass
