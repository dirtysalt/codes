#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        deg = [0] * (n + 1)
        ES = set()

        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
            ES.add((x, y))
            ES.add((y, x))

        ps = []
        for i in range(1, n + 1):
            if deg[i] % 2 == 1:
                ps.append(i)

        sz = len(ps)
        if not sz: return True
        if sz == 2:
            a, b = ps
            if (a, b) not in ES: return True
            for c in range(1, n + 1):
                if c != a and c != b and (a, c) not in ES and (b, c) not in ES:
                    return True
            return False
        elif sz == 4:
            for i in range(1, 4):
                ps[1], ps[i] = ps[i], ps[1]
                a, b = ps[0], ps[1]
                c, d = ps[2], ps[3]
                ps[1], ps[i] = ps[i], ps[1]
                if (a, b) not in ES and (c, d) not in ES:
                    return True
            return False
        return False
