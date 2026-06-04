#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        up = sum(grid[0])
        up -= grid[0][0]
        down = 0
        ans = up
        for i in range(1, n):
            up -= grid[0][i]
            down += grid[1][i - 1]
            res = max(up, down)
            ans = min(ans, res)
        return ans


if __name__ == '__main__':
    pass
