#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        n2 = n * n
        diff = [[0] * (n + 1) for _ in range(n)]
        for (a, b, c, d) in queries:
            for j in range(a, c + 1):
                diff[j][b] += 1
                diff[j][d + 1] -= 1

        values = [[0] * n for _ in range(n)]
        for i in range(n):
            acc = 0
            for j in range(n):
                acc += diff[i][j]
                values[i][j] = acc
        return values


if __name__ == '__main__':
    pass
