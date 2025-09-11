#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def ok(grid):
            values = []
            for g in grid:
                values.append(sum(g))
            total = sum(values)
            upper = 0
            for v in values:
                upper += v
                total -= v
                if upper == total:
                    return True
            return False

        if ok(grid): return True
        if ok(list(zip(*grid))): return True
        return False


if __name__ == '__main__':
    pass
