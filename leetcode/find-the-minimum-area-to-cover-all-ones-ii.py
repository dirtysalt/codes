#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        inf = 1 << 61

        import functools
        @functools.cache
        def find_one(r0, r1, c0, c1):
            res = [r1, r0, c1, c0, 0]
            for r in range(r0, r1 + 1):
                for c in range(c0, c1 + 1):
                    if grid[r][c] == 1:
                        res[0] = min(res[0], r)
                        res[1] = max(res[1], r)
                        res[2] = min(res[2], c)
                        res[3] = max(res[3], c)
                        res[4] += 1
            if res[4] == 0: return inf
            return (res[1] - res[0] + 1) * (res[3] - res[2] + 1)

        def find_two(r0, r1, c0, c1):
            res = inf
            for r in range(r0, r1):
                a = find_one(r0, r, c0, c1)
                b = find_one(r + 1, r1, c0, c1)
                res = min(res, a + b)

            for c in range(c0, c1):
                a = find_one(r0, r1, c0, c)
                b = find_one(r0, r1, c + 1, c1)
                res = min(res, a + b)
            return res

        n, m = len(grid), len(grid[0])
        ANS = inf
        for i in range(n):
            for j in range(m):
                if i == n - 1 and j == m - 1: continue
                ans = inf
                if i == n - 1:
                    res = find_two(0, n - 1, j + 1, m - 1)
                    ans = min(res, ans)
                elif j == m - 1:
                    res = find_two(i + 1, n - 1, 0, m - 1)
                    ans = min(res, ans)
                else:
                    a = find_one(0, n - 1, j + 1, m - 1)
                    b = find_one(i + 1, n - 1, 0, j)
                    ans = min(ans, a + b)

                    c = find_one(i + 1, n - 1, 0, m - 1)
                    d = find_one(0, i, j + 1, m - 1)
                    ans = min(ans, c + d)
                ans += find_one(0, i, 0, j)
                ANS = min(ANS, ans)
        return ANS


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 0, 1], [1, 1, 1]], 5),
    ([[1, 0, 1, 0], [0, 1, 0, 1]], 5),
]

aatest_helper.run_test_cases(Solution().minimumSum, cases)

if __name__ == '__main__':
    pass
