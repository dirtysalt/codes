#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        MS = set()
        for x, y in mines:
            MS.add((x, y))

        A = [[[0] * 4 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            acc = 0
            for j in range(N):
                if (i, j) in MS:
                    acc = 0
                    continue
                acc += 1
                A[i][j][0] = acc
            acc = 0
            for j in reversed(range(N)):
                if (i, j) in MS:
                    acc = 0
                    continue
                acc += 1
                A[i][j][1] = acc
            acc = 0
            for j in range(N):
                if (j, i) in MS:
                    acc = 0
                    continue
                acc += 1
                A[j][i][2] = acc
            acc = 0
            for j in reversed(range(N)):
                if (j, i) in MS:
                    acc = 0
                    continue
                acc += 1
                A[j][i][3] = acc

        ans = 0
        for i in range(N):
            for j in range(N):
                ans = max(ans, min(A[i][j]))
        return ans
