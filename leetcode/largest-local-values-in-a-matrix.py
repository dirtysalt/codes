#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                res = 0
                for k0 in range(3):
                    for k1 in range(3):
                        res = max(res, grid[i + k0][j + k1])
                ans[i][j] = res
        return ans


if __name__ == '__main__':
    pass
