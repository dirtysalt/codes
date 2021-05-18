#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minSwaps(self, s: str) -> int:

        inf = 1 << 30

        def test(t):
            prev = 1
            n = len(t)
            res = 0
            for i in range(n):
                exp = 1 - prev
                if t[i] != exp:
                    off = [i + 1, i + 2]
                    if off[0] % 2 == exp:
                        off[0], off[1] = off[1], off[0]

                    ok = False
                    if not ok:
                        for j in range(off[0], n, 2):
                            if t[j] == exp:
                                t[i], t[j] = t[j], t[i]
                                res += 1
                                ok = True
                                break

                    if not ok:
                        for j in range(off[1], n, 2):
                            if t[j] == exp:
                                t[i], t[j] = t[j], t[i]
                                res += 1
                                ok = True
                                break

                    if not ok: return inf
                prev = exp
            return res

        t = [int(x) for x in s]
        a = test(t)
        t = [1 - int(x) for x in s]
        b = test(t)
        print(a, b)
        ans = min(a, b)
        if ans == inf:
            return -1
        return ans


cases = [
    ("111000", 1),
    ("010", 0),
    ("1110", -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSwaps, cases)

if __name__ == '__main__':
    pass
