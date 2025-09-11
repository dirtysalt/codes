#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        fu = [-1] * n
        ans = []
        cache = {}

        def parent(u, compress=False):
            p = u

            # search
            while fu[p] >= 0:
                p = fu[p]

            # compress
            if compress:
                while u != p:
                    u2 = fu[u]
                    fu[u] = p
                    u = u2

            return p

        def check():
            for x, y in restrictions:
                px = parent(x)
                py = parent(y)
                if px == py:
                    return False
            return True


        for u, v in requests:
            pu = parent(u, compress=True)
            pv = parent(v, compress=True)
            if pu == pv:
                ans.append(True)
                continue

            su = -fu[pu]
            sv = -fu[pv]
            assert su > 0 and sv > 0
            if su > sv:
                pu, pv = pv, pu
                su, sv = sv, su

            fu[pu] = pv
            if check():
                fu[pv] = -(su + sv)
                ans.append(True)
            else:
                fu[pu] = -su
                ans.append(False)

        return ans


if __name__ == '__main__':
    pass
