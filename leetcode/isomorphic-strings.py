#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def ft(x):
            d = {}
            seq = []
            for c in x:
                if c not in d:
                    v = len(d)
                    d[c] = v
                else:
                    v = d[c]
                seq.append(v)
            return tuple(seq)

        a = ft(s)
        b = ft(t)
        return a == b
