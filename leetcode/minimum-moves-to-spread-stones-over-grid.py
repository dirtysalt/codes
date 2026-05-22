#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def next(st):
            st = list(st)
            a, b = [], []
            for i in range(9):
                if st[i] != 1:
                    c = a if st[i] != 0 else b
                    c.append(i)

            for i in a:
                for j in b:
                    # move one from a->b
                    st[i] -= 1
                    st[j] += 1
                    d = abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
                    yield d, tuple(st)
                    st[i] += 1
                    st[j] -= 1

        st = []
        for i in range(3):
            for j in range(3):
                st.append(grid[i][j])
        st = tuple(st)

        Q = []
        Q.append((0, st))
        dep = {}
        while Q:
            d, st = heapq.heappop(Q)
            if st == (1, 1, 1, 1, 1, 1, 1, 1, 1):
                return d
            dep[st] = d
            for d2, st2 in next(st):
                if st2 in dep: continue
                heapq.heappush(Q, (d2 + d, st2))


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1, 0], [1, 1, 1], [1, 2, 1]], 3),
    ([[1, 3, 0], [1, 0, 0], [1, 0, 3]], 4),
    ([[1, 2, 2], [1, 1, 0], [0, 1, 1]], 4),
]

aatest_helper.run_test_cases(Solution().minimumMoves, cases)

if __name__ == '__main__':
    pass
