#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        values = []
        from collections import defaultdict
        rpos = [defaultdict(list) for _ in range(n)]
        cpos = [defaultdict(list) for _ in range(m)]
        rnext = [{} for _ in range(n)]
        cnext = [{} for _ in range(m)]

        for i in range(n):
            for j in range(m):
                x = mat[i][j]
                rpos[i][x].append((i, j))
                cpos[j][x].append((i, j))
                values.append((x, i, j))

        END = -10 ** 9

        def build_next(sz, pos, next):
            for i in range(sz):
                keys = list(pos[i])
                keys.sort(reverse=True)
                keys.append(END)
                nn = next[i]
                for idx in range(1, len(keys)):
                    x, y = keys[idx - 1], keys[idx]
                    nn[x] = y

        build_next(n, rpos, rnext)
        build_next(m, cpos, cnext)

        ans = [[0] * m for _ in range(n)]
        values.sort(reverse=True)

        def check(next, pos, x):
            y = next[x]
            for r, c in pos[y]:
                yield r, c

        for x, i, j in values:
            d = ans[i][j]
            for r, c in check(rnext[i], rpos[i], x):
                ans[r][c] = max(ans[r][c], d + 1)
            for r, c in check(cnext[j], cpos[j], x):
                ans[r][c] = max(ans[r][c], d + 1)

        r = max((max(x) for x in ans))
        return r + 1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[3, 1], [3, 4]], 2),
    ([[1, 1], [1, 1]], 1),
    ([[3, 1, 6], [-9, 5, 7]], 4),
]

aatest_helper.run_test_cases(Solution().maxIncreasingCells, cases)

if __name__ == '__main__':
    pass
