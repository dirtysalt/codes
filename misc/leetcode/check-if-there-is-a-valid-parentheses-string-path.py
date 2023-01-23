#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])

        import functools
        @functools.lru_cache(maxsize=None)
        def dfs(i, j, d):
            if i == n or j == m:
                return False
            c = grid[i][j]
            d += (1 if c == '(' else -1)
            if d < 0:
                return False
            if (i, j) == (n - 1, m - 1):
                return d == 0
            return dfs(i + 1, j, d) or dfs(i, j + 1, d)

        return dfs(0, 0, 0)


true, false, null = True, False, None
cases = [
    ([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]], true),
    ([[")", ")"], ["(", "("]], false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().hasValidPath, cases)

if __name__ == '__main__':
    pass
