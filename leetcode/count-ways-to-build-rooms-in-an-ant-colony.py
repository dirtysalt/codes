#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Tree:
    def __init__(self, idx):
        self.idx = idx
        self.child = []
        self.n = 1
        self.val = 1


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        # n个节点并且n-1条边，并且0可以访问到所有房间，说明是个树结构
        n = len(prevRoom)
        ind = [0] * n
        for x in prevRoom:
            if x == -1: continue
            ind[x] += 1

        # build tree by top sort.
        from collections import deque
        dq = deque()
        for i in range(n):
            if ind[i] == 0:
                dq.append(i)
        trees = []
        for i in range(n):
            trees.append(Tree(i))

        while dq:
            x = dq.popleft()
            p = prevRoom[x]
            if p == -1: continue
            t = trees[x]
            pt = trees[p]
            pt.child.append(t)
            ind[p] -= 1
            if ind[p] == 0:
                dq.append(p)

        MOD = 10 ** 9 + 7
        fac = [0] * (n + 1)
        rev = [0] * (n + 1)

        t = 1
        for i in range(1, n + 1):
            t = (t * i) % MOD
            fac[i] = t

        def pow(x, y):
            t = 1
            while y:
                if y & 0x1:
                    t = (t * x) % MOD
                x = (x * x) % MOD
                y = y >> 1
            return t

        for i in range(1, n + 1):
            rev[i] = pow(fac[i], MOD - 2)

        # print(fac, rev)

        def compute(t):
            if len(t.child) == 0:
                return

            # 假设有3个子节点，A, B, C
            # 每个节点下面排列分别是Na, Nb, Nc
            # 那么总排列是 (A+B+C)! / (A! * B! * C!) * (Na * Nb * Nc)
            n = 0
            b = 1
            for c in t.child:
                compute(c)
                n += c.n
                b = (b * rev[c.n] * c.val) % MOD
            t.n = n + 1
            t.val = (fac[n] * b) % MOD
            return

        compute(trees[0])
        ans = trees[0].val
        return ans


true, false, null = True, False, None
cases = [
    ([-1, 0, 1], 1),
    ([-1, 0, 0, 1, 2], 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().waysToBuildRooms, cases)

if __name__ == '__main__':
    pass
