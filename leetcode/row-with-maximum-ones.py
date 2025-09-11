#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        M, A = 0, 0
        for i in range(n):
            t = sum(mat[i])
            if t > M:
                A = i
                M = t
        return [A, M]


if __name__ == '__main__':
    pass
