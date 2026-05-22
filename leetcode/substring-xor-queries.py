#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        INF = 10 ** 10
        s = [int(x) for x in s]
        pos = {}
        last = 0
        for i in range(len(s)):
            if s[i] == 1:
                val, j = 0, i
                while j < len(s) and val < INF:
                    val = val * 2 + s[j]
                    if val not in pos:
                        # pos[val] = (last, j)
                        pos[val] = (i, j)
                    j += 1
            else:
                if 0 not in pos:
                    pos[0] = (i, i)

            if s[last] == 0:
                pass
            else:
                last = i

        # print(pos)

        def handle(q):
            a, b = q
            c = a ^ b
            if c not in pos:
                return [-1, -1]
            (i, j) = pos[c]
            return [i, j]

        ans = []
        for q in queries:
            r = handle(q)
            ans.append(r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("101101", [[0, 5], [1, 2]], [[0, 2], [2, 3]]),
    ("0101", [[12, 8]], [[-1, -1]]),
    ("1", [[4, 5]], [[0, 0]]),
]

aatest_helper.run_test_cases(Solution().substringXorQueries, cases)

if __name__ == '__main__':
    pass
