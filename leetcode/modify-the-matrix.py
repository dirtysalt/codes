#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        M = [-2] * m
        for j in range(m):
            for i in range(n):
                M[j] = max(M[j], matrix[i][j])

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[i][j]
                if ans[i][j] == -1:
                    ans[i][j] = M[j]

        return ans


if __name__ == '__main__':
    pass
