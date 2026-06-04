#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        mark = [0] * n

        def visit(x, c):
            mark[x] = c
            for y in range(n):
                if M[x][y] and not mark[y]:
                    visit(y, c)

        ans = 0
        for i in range(n):
            if mark[i]: continue
            visit(i, ans + 1)
            ans += 1
        return ans
