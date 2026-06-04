#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        r, c = set(), set()
        ans = 0
        for t, i, v in reversed(queries):
            if t == 0:
                if i in r: continue
                ans += v * (n - len(c))
                r.add(i)
            else:
                if i in c: continue
                ans += v * (n - len(r))
                c.add(i)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]], 23),
    (3, [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]], 17),
]

aatest_helper.run_test_cases(Solution().matrixSumQueries, cases)

if __name__ == '__main__':
    pass
