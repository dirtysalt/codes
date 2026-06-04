#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def coloredCells(self, n: int) -> int:
        # f(n) = f(n-1) + 4(n-1)
        # f(1) = 1
        ans = 1 + 2 * (n - 1) * n
        return ans


if __name__ == '__main__':
    pass
