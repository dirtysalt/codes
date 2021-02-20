#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        # write your code here
        k = len(operators)
        nm = n * m
        if nm == 0:
            return [0] * k
        st = [-1] * (nm)

        def rc2idx(r, c):
            return r * m + c

        def compress(st, idx, min_idx):
            while st[idx] != idx:
                pp = st[idx]
                st[idx] = min_idx
                idx = pp
            st[idx] = min_idx

        def query(st, idx):
            pp = idx
            while st[pp] != pp:
                pp = st[pp]
            return pp

        res = []
        components = set()
        for op in operators:
            (r, c) = op.x, op.y
            idx = rc2idx(r, c)
            st[idx] = idx

            connects = []
            connects.append(idx)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < m:
                    idx = rc2idx(nr, nc)
                    if st[idx] != -1:
                        connects.append(idx)

            query_idxs = []
            for idx in connects:
                query_idx = query(st, idx)
                query_idxs.append(query_idx)

            min_query_idx = min(query_idxs)
            for query_idx in query_idxs:
                st[query_idx] = min_query_idx
                if query_idx in components:
                    components.remove(query_idx)

            components.add(min_query_idx)
            res.append(len(components))
        return res
