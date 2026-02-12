#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(i, j, x, y):
            a, b = 0, 0
            if i == x and j == y:
                if grid[i][j] == 0:
                    a += 1
                else:
                    b += 1
                return Node(grid[i][j], True, None, None, None, None), a, b

            sz = (x - i + 1) // 2
            tl, aa, bb = build(i, j, i + sz - 1, j + sz - 1)
            a, b = a + aa, b + bb

            tr, aa, bb = build(i, j + sz, i + sz - 1, y)
            a, b = a + aa, b + bb

            bl, aa, bb = build(i + sz, j, x, j + sz - 1)
            a, b = a + aa, b + bb

            br, aa, bb = build(i + sz, j + sz, x, y)
            a, b = a + aa, b + bb

            v = -1
            if a == (x - i + 1) ** 2:
                v = 0
            if b == (x - i + 1) ** 2:
                v = 1

            if v != -1:
                return Node(v, True, None, None, None, None), a, b

            return Node(v, False, tl, tr, bl, br), a, b

        ans, _, _ = build(0, 0, n - 1, n - 1)
        return ans
