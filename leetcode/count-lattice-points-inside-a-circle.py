#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()

        for x, y, r in circles:
            r2 = r ** 2
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i, j) in s: continue
                    if (i - x) ** 2 + (j - y) ** 2 <= r2:
                        s.add((i, j))

        return len(s)

if __name__ == '__main__':
    pass
