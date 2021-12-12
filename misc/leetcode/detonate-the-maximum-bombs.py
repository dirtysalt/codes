#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        mat = [[0] * n for _ in range(n)]

        def match(i, j):
            x, y, r = bombs[i]
            x0, y0, _ = bombs[j]
            return (x - x0) ** 2 + (y - y0) ** 2 <= r * r

        for i in range(n):
            for j in range(n):
                mat[i][j] = 1 if match(i, j) else 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if not mat[i][j] and mat[i][k] and mat[k][j]:
                        mat[i][j] = 1

        ans = 0
        for i in range(n):
            acc = sum(mat[i])
            ans = max(ans, acc)
        return ans


if __name__ == '__main__':
    pass
