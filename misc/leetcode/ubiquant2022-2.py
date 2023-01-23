#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def lakeCount(self, field: List[str]) -> int:

        n, m = len(field), len(field[0])
        mask = [[0] * m for _ in range(n)]

        def dfs(i, j, r):
            if mask[i][j]:
                return
            mask[i][j] = r

            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if (dx, dy) == (0, 0): continue
                    i2, j2 = i + dx, j + dy
                    if 0 <= i2 < n and 0 <= j2 < m and field[i2][j] == 'W':
                        dfs(i2, j2, r)

        r = 0
        for i in range(n):
            for j in range(m):
                if mask[i][j] == 0 and field[i][j] == 'W':
                    r += 1
                    dfs(i, j, r)
        return r
    

if __name__ == '__main__':
    pass
