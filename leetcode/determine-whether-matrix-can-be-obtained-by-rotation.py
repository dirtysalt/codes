#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def tr(i, j):
            return (i, j), (j, n-1-i), (n-1-i, n-j-1), (n-j-1, i)

        for idx in range(4):
            ok = True
            for i in range(n):
                for j in range(n):
                    trs = tr(i, j)
                    i2, j2 = trs[idx]
                    if mat[i][j] != target[i2][j2]:
                        ok = False
                        break
                if not ok: break
            if ok: return True
        return False

if __name__ == '__main__':
    pass
