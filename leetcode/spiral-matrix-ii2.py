#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        i, j, k, d = 0, -1, n, 0
        dxy = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        v = 1
        while k >= 1:
            dx, dy = dxy[d]
            for _ in range(k):
                i, j = i + dx, j + dy
                ans[i][j] = v
                # print(i, j, v)
                v += 1

            dx, dy = dxy[d + 1]
            for _ in range(k - 1):
                i, j = i + dx, j + dy
                ans[i][j] = v
                # print(i, j, v)
                v += 1

            d = (d + 2) % 4
            k -= 1
        return ans
