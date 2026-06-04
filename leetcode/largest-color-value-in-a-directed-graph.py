#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]
        inc = [0] * n
        for x, y in edges:
            adj[x].append(y)
            inc[y] += 1

        def check_cycle():
            inc2 = inc.copy()
            dq = deque()
            for x in range(n):
                if inc2[x] == 0:
                    dq.append(x)

            while dq:
                x = dq.popleft()
                for y in adj[x]:
                    inc2[y] -= 1
                    if inc2[y] == 0:
                        dq.append(y)

            for x in range(n):
                if inc2[x] != 0:
                    return False

            return True

        if not check_cycle():
            return -1

        cache = {}

        def visit(x):
            if x in cache: return cache[x]
            rs = [0] * 26
            v = ord(colors[x]) - ord('a')
            for y in adj[x]:
                rs2 = visit(y)
                for i in range(26):
                    rs[i] = max(rs[i], rs2[i])
            rs[v] += 1
            cache[x] = rs
            return rs

        ans = 0
        for x in range(n):
            if inc[x] == 0:
                res = visit(x)
                ans = max(ans, max(res))

        return ans


cases = [
    ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3),
    ("a", [[0, 0]], -1),
    ("hhqhuqhqff",
     [[0, 1], [0, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7], [6, 7], [7, 8], [3, 8], [5, 8], [8, 9], [3, 9], [6, 9]],
     3),
    ("hhhhkkkhkh",
     [[0, 1], [0, 2], [1, 2], [2, 3], [1, 3], [3, 4], [3, 5], [4, 5], [3, 6], [5, 6], [2, 6], [4, 6], [3, 7], [6, 7],
      [7, 8], [6, 8], [8, 9], [6, 9]], 6),
    ("nnllnzznn",
     [[0, 1], [1, 2], [2, 3], [2, 4], [3, 5], [4, 6], [3, 6], [5, 6], [6, 7], [7, 8]], 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestPathValue, cases)

if __name__ == '__main__':
    pass
