#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n, m = len(board), len(board[0])
        MAX_VAL = [[0] * m for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(m):
                MAX_VAL[i][j] = board[i][j]
                if (i + 1) < n:
                    MAX_VAL[i][j] = max(MAX_VAL[i][j], MAX_VAL[i + 1][j])

        MAX_COL = [[] for _ in range(n)]
        COLS = set()
        for i in range(n):
            js = list(range(m))
            js.sort(key=lambda x: board[i][x], reverse=True)
            MAX_COL[i] = js[:3]
            COLS.update(js[:3])

        COLS = list(COLS)

        import functools
        @functools.cache
        def getmax(st, i, k):
            xs = []
            for j in COLS:
                if st & (1 << j) == 0:
                    xs.append(MAX_VAL[i][j])
            xs.sort()
            return sum(xs[-k:])

        inf = 1 << 63
        ans = -inf

        def dfs(st, i, k, now):
            nonlocal ans
            if i == n: return
            bound = getmax(st, i, k)
            if k == 1:
                ans = max(ans, bound + now)
                return
            # cut branch
            if now + bound <= ans:
                return

            for ii in range(i, n):
                for j in MAX_COL[ii]:
                    if st & (1 << j): continue
                    v = board[ii][j]
                    dfs(st | (1 << j), ii + 1, k - 1, now + v)

        dfs(0, 0, 3, 0)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]], 4),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
    ([[-53, -86, -80], [-28, 16, -42], [-88, 38, -66]], -57)
]

aatest_helper.run_test_cases(Solution().maximumValueSum, cases)

if __name__ == '__main__':
    pass
