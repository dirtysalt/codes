#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import copy
from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def add(g, d):
            for i in range(len(g)):
                for j in range(len(g[i])):
                    g[i][j] += d
            return g

        def concat(a, b, c, d):
            n = len(a)
            g = [[0] * (2 * n) for _ in range(2 * n)]
            for i in range(n):
                for j in range(n):
                    g[i][j] = a[i][j]
                    g[i][j + n] = b[i][j]
                    g[i + n][j] = c[i][j]
                    g[i + n][j + n] = d[i][j]
            return g

        def gen(n):
            if n == 0:
                return [[0]]
            a = gen(n - 1)
            delta = 1 << (2 * (n - 1))
            b = add(copy.deepcopy(a), delta)
            c = add(copy.deepcopy(b), delta)
            d = add(copy.deepcopy(c), delta)
            return concat(d, a, c, b)

        ans = gen(n)
        # for g in ans:
        #     print(g)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (1, [[3, 0], [2, 1]]),
    (2, [[15, 12, 3, 0], [14, 13, 2, 1], [11, 8, 7, 4], [10, 9, 6, 5]])
]

aatest_helper.run_test_cases(Solution().specialGrid, cases)

if __name__ == '__main__':
    pass
