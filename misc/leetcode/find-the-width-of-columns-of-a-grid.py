#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ans = [0] * m
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                d = 0
                if v < 0:
                    d += 1
                    v = -v
                if v == 0: d += 1
                while v:
                    d += 1
                    v = v // 10
                ans[j] = max(ans[j], d)
        return ans


if __name__ == '__main__':
    pass
