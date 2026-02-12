#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        d = Counter()

        for x in grid:
            tx = tuple(x)
            d[tx] += 1

        grid2 = zip(*grid)
        ans = 0
        for x in grid2:
            tx = tuple(x)
            if tx in d:
                ans += d[tx]

        return ans


if __name__ == '__main__':
    pass
