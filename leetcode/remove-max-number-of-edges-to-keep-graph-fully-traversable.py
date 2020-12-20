#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = [0] * (n + 1)
        B = [0] * (n + 1)

        def merge(fu, x, y):
            if x == y: return
            fu[x] = y

        def parent(fu, x):
            p = x
            while fu[p] != 0:
                p = fu[p]

            while x != p:
                x2 = fu[x]
                fu[x] = p
                x = x2
            return p

        edges = [tuple(x) for x in edges]
        edges.sort(reverse=True)
        c = 0
        for t, x, y in edges:
            if t == 3:
                p1 = parent(A, x)
                p2 = parent(A, y)
                p3 = parent(B, x)
                p4 = parent(B, y)
                if (p1 != p2) or (p3 != p4):
                    c += 1
                    merge(A, p1, p2)
                    merge(B, p3, p4)

            elif t == 1:
                p1 = parent(A, x)
                p2 = parent(A, y)
                if p1 != p2:
                    c += 1
                    merge(A, p1, p2)

            else:
                p1 = parent(B, x)
                p2 = parent(B, y)
                if p1 != p2:
                    c += 1
                    merge(B, p1, p2)

        p0 = parent(A, 1)
        p1 = parent(B, 1)
        for i in range(1, n + 1):
            p = parent(A, i)
            if p != p0: return -1
            p = parent(B, i)
            if p != p1: return -1

        ans = len(edges) - c
        return ans
