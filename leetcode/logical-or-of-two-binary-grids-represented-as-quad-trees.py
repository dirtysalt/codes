#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        null = None

        def make(val, isLeaf, c):
            return Node(val, isLeaf, c[0], c[1], c[2], c[3])

        null4 = [null] * 4

        def build(q1, q2):
            if q1.isLeaf and q2.isLeaf:
                return make(q1.val | q2.val, True, null4)

            a = [q1.topLeft, q1.topRight, q1.bottomLeft, q1.bottomRight]
            if q1.isLeaf:
                x = make(q1.val, True, null4)
                a = [x] * 4
            b = [q2.topLeft, q2.topRight, q2.bottomLeft, q2.bottomRight]
            if q2.isLeaf:
                x = make(q2.val, True, null4)
                b = [x] *4

            c = []
            for i in range(4):
                c.append(build(a[i], b[i]))
            allLeaf = all((c[i].isLeaf for i in range(4)))
            if allLeaf:
                same = True
                for i in range(1,4):
                    if c[i].val != c[0].val:
                        same = False
                        break
                if same:
                    return make(c[0].val, True, null4)
            return make(null, False, c)

        ans = build(quadTree1, quadTree2)
        return ans


if __name__ == '__main__':
    pass
