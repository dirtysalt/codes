#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            grid[i].sort()

        ans = 0
        for _ in range(m):
            res = max((grid[i][-1] for i in range(n)))
            ans += res
            for i in range(n):
                grid[i].pop()
        return ans


if __name__ == '__main__':
    pass
