#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        qcoords = set([tuple(x) for x in queens])
        n, m = 8, 8

        for dx, dy in [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]:
            if (dx, dy) == (0, 0):
                continue
            x, y = king
            while 0 <= x < n and 0 <= y < m:
                if (x, y) in qcoords:
                    ans.append([x, y])
                    break
                x += dx
                y += dy
        return ans
