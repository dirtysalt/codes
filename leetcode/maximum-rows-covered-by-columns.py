#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for st in range(1 << n):
            c = 0
            for j in range(n):
                if st & (1 << j): c += 1
            if c != cols: continue

            c = 0
            for i in range(m):
                t0, t1 = 0, 0
                for j in range(n):
                    if mat[i][j] == 0: continue
                    t0 += 1
                    if st & (1 << j):
                        t1 += 1
                if t0 == t1:
                    c += 1
            ans = max(ans, c)
        return ans


if __name__ == '__main__':
    pass
