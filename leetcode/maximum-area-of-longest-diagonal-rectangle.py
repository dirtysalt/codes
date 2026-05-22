#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        diag = 0
        for x, y in dimensions:
            d = x * x + y * y
            if d == diag:
                ans = max(ans, x * y)
            elif d > diag:
                diag = d
                ans = x * y
        return ans


if __name__ == '__main__':
    pass
