#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def test(G):
            n, m = len(G), len(G[0])
            ans = 0
            for i in range(n):
                for j in range(m // 2):
                    if G[i][j] != G[i][m - 1 - j]:
                        ans += 1
            return ans

        transposed = list(zip(*grid))
        a = test(grid)
        b = test(transposed)
        return min(a, b)


if __name__ == '__main__':
    pass
