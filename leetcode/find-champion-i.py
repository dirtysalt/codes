#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ind = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if grid[i][j] == 1:
                    ind[j] += 1
                else:
                    ind[i] += 1
        for i in range(n):
            if ind[i] == 0: return i
        return -1


if __name__ == '__main__':
    pass
