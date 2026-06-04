#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []

        data = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                data[i][j] = original[i * n + j]

        return data


if __name__ == '__main__':
    pass
