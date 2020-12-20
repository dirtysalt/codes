#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rows = [0] * n
        cols = [0] * m
        ans = [[0] * m for _ in range(n)]

        tmp = []
        for i in range(n):
            for j in range(m):
                tmp.append((matrix[i][j], i, j))
        tmp.sort()

        # 主要是处理相同值的rank，为此需要将相同值全部group起来
        # 然后查找可能的联通分量，相同联通分量的rank是相同的，也是使用最大值
        import itertools
        for _, _g in itertools.groupby(tmp, key=lambda x: x[0]):
            g = list(_g)
            sz = len(g)
            visited = [0] * sz
            from collections import defaultdict
            ri = defaultdict(list)
            ci = defaultdict(list)

            for k in range(sz):
                _, i, j = g[k]
                ri[i].append(k)
                ci[j].append(k)

            def dfs(k, res):
                visited[k] = 1
                res.append(k)
                _, i, j = g[k]
                for k2 in ri[i]:
                    if not visited[k2]:
                        dfs(k2, res)
                for k2 in ci[j]:
                    if not visited[k2]:
                        dfs(k2, res)

            def mark(res):
                r = 0
                for k2 in res:
                    _, i, j = g[k2]
                    r2 = max(rows[i], cols[j]) + 1
                    r = max(r, r2)
                for k2 in res:
                    _, i, j = g[k2]
                    rows[i] = r
                    cols[j] = r
                    ans[i][j] = r

            for k in range(sz):
                if not visited[k]:
                    res = []
                    dfs(k, res)
                    mark(res)

        return ans


cases = [
    ([[1, 2], [3, 4]], [[1, 2], [2, 3]]),
    ([[7, 7], [7, 7]], [[1, 1], [1, 1]]),
    ([[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]], [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]]),
    ([[7, 3, 6], [1, 4, 5], [9, 8, 2]], [[5, 1, 4], [1, 2, 3], [6, 3, 1]]),
    ([[-37, -50, -3, 44], [-37, 46, 13, -32], [47, -42, -3, -40], [-17, -22, -39, 24]],
     [[2, 1, 4, 6], [2, 6, 5, 4], [5, 2, 4, 3], [4, 3, 1, 5]]),
    ([[-23, 20, -49, -30, -39, -28, -5, -14], [-19, 4, -33, 2, -47, 28, 43, -6], [-47, 36, -49, 6, 17, -8, -21, -30],
      [-27, 44, 27, 10, 21, -8, 3, 14], [-19, 12, -25, 34, -27, -48, -37, 14], [-47, 40, 23, 46, -39, 48, -41, 18],
      [-27, -4, 7, -10, 9, 36, 43, 2], [37, 44, 43, -38, 29, -44, 19, 38]],
     [[7, 13, 1, 5, 4, 6, 9, 8], [8, 11, 2, 10, 1, 12, 14, 9], [2, 14, 1, 11, 13, 7, 5, 3],
      [3, 19, 16, 12, 14, 7, 10, 13], [8, 12, 6, 14, 5, 1, 4, 13], [2, 16, 15, 17, 4, 18, 3, 14],
      [3, 7, 11, 6, 12, 13, 14, 10], [16, 19, 18, 3, 15, 2, 11, 17]]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().matrixRankTransform, cases)
