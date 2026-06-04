#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def flip(grid):
            return grid[::-1]

        def transpose(grid):
            return list(zip(*grid))

        def ok(grid):
            values = []
            from collections import Counter
            cnt = Counter()
            n, m = len(grid), len(grid[0])
            for g in grid:
                values.append(sum(g))
                for x in g:
                    cnt[x] += 1

            total = sum(values)
            upper = 0
            for i in range(n):
                v = values[i]
                upper += v
                total -= v
                for x in grid[i]:
                    cnt[x] -= 1
                if upper == total:
                    return True
                if total > upper:
                    rest = (n - 1 - i)
                    diff = total - upper
                    if rest >= 2:
                        if m >= 2 and cnt[diff]: return True
                        if m == 1 and diff in (grid[i + 1][0], grid[-1][0]): return True
                    if rest == 1 and diff in (grid[-1][0], grid[-1][-1]):
                        return True
            return False

        if ok(grid): return True
        if ok(flip(grid)): return True
        trans = transpose(grid)
        if ok(trans): return True
        if ok(flip(trans)): return True
        return False


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 2, 4], [2, 3, 5]], false),
    ([[1, 2], [3, 4]], true),
    ([[1, 4], [2, 3]], true),
    ([[25372], [100000], [100000]], true),
    ([[100000], [100000], [25372], ], true),

]

aatest_helper.run_test_cases(Solution().canPartitionGrid, cases)

if __name__ == '__main__':
    pass
