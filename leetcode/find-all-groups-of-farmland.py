#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        ans = []
        if n == 0: return ans
        m = len(land[0])

        def find(x, y):
            while x < n and land[x][y] == 1:
                x += 1
            x -= 1
            while y < m and land[x][y] == 1:
                y += 1
            y -= 1
            return x, y

        visited = set()

        def mark(x0, y0, x1, y1):
            for i in range(x0, x1 + 1):
                for j in range(y0, y1 + 1):
                    visited.add((i, j))

        for x in range(n):
            for y in range(m):
                if land[x][y] == 1 and (x, y) not in visited:
                    x2, y2 = find(x, y)
                    ans.append([x, y, x2, y2])
                    mark(x, y, x2, y2)

        return ans


if __name__ == '__main__':
    pass
